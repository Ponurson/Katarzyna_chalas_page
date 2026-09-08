#!/usr/bin/env python3
"""Export editable content of the nine static pages; never import or modify HTML.

python3 tools/make_content_template.py [--check] [--output PATH]
Dependencies: openpyxl. Full instructions: README.md.
"""
import argparse
from dataclasses import dataclass, field, replace
from html.parser import HTMLParser
from pathlib import Path
import re

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter

ROOT = Path(__file__).resolve().parent.parent
PAGES = (
    'index.html', 'moja-droga.html', 'twoja-droga.html', 'coaching.html',
    'interwencja-kryzysowa.html', 'prism-brain-mapping.html', 'mtq-plus.html',
    'terapia-dzwiekiem.html', 'warsztaty-i-szkolenia.html',
)
OUT = ROOT / 'teksty-strony.xlsx'
CHROME = {'Menu', 'Stopka'}  # wspólny nagłówek i stopka: jeden komplet wierszy zamiast dziewięciu kopii
SHARED = 'wszystkie strony'
VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr'}
SKIP = {'svg', 'script', 'style', 'template'}
OWNERS = {'title', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'dt', 'dd', 'figcaption', 'button', 'cite', 'a', 'span', 'small', 'strong', 'em', 'blockquote', 'address'}
BLOCKS = {'p', 'ul', 'ol', 'dl', 'div', 'section', 'article', 'blockquote'}
LABELS = {'title': 'Tytuł strony', 'p': 'Akapit', 'h1': 'Nagłówek H1', 'h2': 'Nagłówek H2', 'h3': 'Nagłówek H3', 'li': 'Punkt listy', 'dt': 'Usługa / termin', 'dd': 'Cena / opis', 'cite': 'Autor cytatu', 'figcaption': 'Podpis ilustracji', 'a': 'Etykieta linku', 'button': 'Etykieta przycisku', 'span': 'Etykieta', 'strong': 'Wyróżnienie / nazwa', 'small': 'Podpis'}


def normal(text):
    return ' '.join(text.replace('\xa0', ' ').split())


@dataclass(eq=False)  # parent/children cycle: compare nodes by identity
class Node:
    tag: str
    attrs: dict = field(default_factory=dict)
    parent: object = None
    children: list = field(default_factory=list)

    def ancestors(self):
        node = self.parent
        while node:
            yield node
            node = node.parent

    def hidden(self):
        return any(n.tag in SKIP or n.attrs.get('aria-hidden') == 'true' or 'hidden' in n.attrs for n in [self, *self.ancestors()])

    def text(self, own=False):
        return normal(self.raw_text(own))

    def raw_text(self, own=False):
        chunks = []
        for child in self.children:
            if isinstance(child, str):
                chunks.append(child)
            elif not child.hidden():
                if own and child.tag in BLOCKS:
                    continue
                chunks.append(' ' if child.tag == 'br' else child.raw_text(own))
                if child.tag in BLOCKS or child.tag == 'li':
                    chunks.append(' ')
        return ''.join(chunks)

    def walk(self):
        for child in self.children:
            if isinstance(child, Node):
                yield child
                yield from child.walk()

    def selector(self):
        if self.attrs.get('data-content-id'):
            return f'{self.tag}[data-content-id="{self.attrs["data-content-id"]}"]'
        if self.attrs.get('id'):
            return f'{self.tag}[id="{self.attrs["id"]}"]'
        siblings = [n for n in self.parent.children if isinstance(n, Node) and n.tag == self.tag]
        part = f'{self.tag}:nth-of-type({siblings.index(self) + 1})'
        return (self.parent.selector() + ' > ' if self.parent.tag != 'document' else '') + part

    def section(self):
        for n in [self, *self.ancestors()]:
            if n.attrs.get('data-section'):
                return n.attrs['data-section']
            if n.tag == 'header':
                return 'Menu'
            if n.tag == 'footer':
                return 'Stopka'
        return 'Ustawienia strony'


class Document(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.root = Node('document')
        self.current = self.root
        self.feed(text)
        self.close()

    def handle_starttag(self, tag, attrs):
        node = Node(tag, dict(attrs), self.current)
        self.current.children.append(node)
        if tag not in VOID:
            self.current = node

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for node in [self.current, *self.current.ancestors()]:
            if node.tag == tag:
                self.current = node.parent
                return

    def handle_data(self, data):
        self.current.children.append(data)

    @property
    def nodes(self):
        return list(self.root.walk())


@dataclass
class Row:
    id: str
    page: str
    section: str
    kind: str
    text: str
    context: str
    attribute: str

    def values(self):
        return [self.id, self.page, self.section, self.kind, self.text, '', '', self.context, self.attribute]


def extract(page, text):
    doc = Document(text)
    result = []
    for node in doc.nodes:
        if node.hidden():
            continue
        key = node.attrs.get('data-content-id') or node.attrs.get('id') or node.selector()
        def add(kind, value, attribute):
            value = normal(value or '')
            if value or attribute == 'alt':
                context = node.selector()
                if node.tag == 'a':
                    context += ' | ' + node.text() + ' → ' + node.attrs.get('href', '')
                if node.tag == 'img':
                    context += ' | ' + node.attrs.get('src', '')
                result.append(Row(f'{Path(page).stem}:{key}:{attribute}', page, node.section(), kind, value, context, attribute))
        if node.tag == 'meta' and node.attrs.get('name') == 'description':
            add('Opis strony (meta description)', node.attrs.get('content'), 'content')
        if node.tag == 'img':
            add('Opis obrazu (alt)', node.attrs.get('alt'), 'alt')
        if node.tag == 'a' and 'href' in node.attrs:
            add('Adres linku', node.attrs['href'], 'href')
        for attr in ('aria-label', 'title'):
            if attr in node.attrs:
                add('Etykieta dostępności' if attr == 'aria-label' else 'Podpowiedź', node.attrs[attr], attr)
        if node.tag not in OWNERS:
            continue
        # A paragraph owns its inline emphasis/link label. The link href is still
        # exported above. Nested lists own their items; no duplicated paragraphs.
        if any(a.tag in OWNERS and a.tag not in {'li', 'blockquote', 'address'} for a in node.ancestors()):
            continue
        if node.tag in {'li', 'blockquote', 'address'}:
            content = node.text(own=True)
        else:
            content = node.text()
        if content:
            add(LABELS.get(node.tag, node.tag), content, 'text')
    return result


def anchor(href):
    """Menu i stopka: index kotwiczy w sobie, podstrony przez index.html."""
    return href.removeprefix('index.html') or '#top'


def chrome_key(row):
    return (row.id.split(':', 1)[1], row.section, row.kind, row.attribute,
            anchor(row.text) if row.attribute == 'href' else row.text)


def extract_site():
    shared, own = [], []
    for page in PAGES:
        for row in extract(page, (ROOT / page).read_text(encoding='utf-8')):
            if row.section not in CHROME:
                own.append(row)
            elif page == PAGES[0]:  # index.html jest wzorcem wspólnego menu i stopki
                shared.append(replace(row, id='wspolne:' + row.id.split(':', 1)[1], page=SHARED))
    return shared + own


def build(rows, output=OUT):
    if output.exists():
        old = load_workbook(output, read_only=True, data_only=False)
        filled = 'Teksty' in old and any(r[5] or r[6] for r in old['Teksty'].iter_rows(min_row=2, values_only=True) if len(r) >= 7)
        old.close()
        if filled:
            raise ValueError('Plik ma wypełnione kolumny F/G. Zachowaj go i użyj --output z nową nazwą.')
    wb = Workbook()
    info = wb.active
    info.title = 'Instrukcja'
    info.column_dimensions['A'].width = 120
    instructions = [
        'WZORZEC TEKSTÓW — Katarzyna Chałas — 9 stron',
        'Wypełnij NOWY TEKST (F) i ewentualnie UWAGI (G) w arkuszu Teksty.',
        'Puste pole = bez zmiany. USUŃ = usuń wskazany element HTML (w wierszu atrybutu także cały element, np. link).',
        'Nie zmieniaj ID ani kolumn opisujących obecną stronę. Nie skracaj tekstów do dawnych limitów.',
        'ID = nazwa pliku bez .html : data-content-id elementu : pole (text, href, alt, content, aria-label).',
        'Menu i stopka są wspólne dla dziewięciu stron: mają jeden komplet wierszy "wszystkie strony" i ID wspolne:… — zmiana obowiązuje wszędzie.',
        'Odnośniki menu i stopki zapisano jak na stronie głównej; na podstronach ten sam odnośnik ma prefiks index.html (np. index.html#kontakt).',
        'Strona, sekcja i selektor HTML w kontekście rozróżniają identyczne nagłówki, etykiety i przyciski.',
        'Pełne akapity zawierają także wyróżnienia i teksty linków. Zmiana treści wymaga zachowania formatowania i linków w HTML.',
        'Adres każdego linku (także wewnętrznego) ma osobny wiersz href. Tekst zagnieżdżonego linku znajduje się w jego akapicie.',
        'Cennik: nazwa usługi i cena są osobnymi wierszami dt/dd. Punkty podlist są osobnymi wierszami.',
        'Zmiany stosuje wykonawca ręcznie po ID + stronie + polu. Projekt nie zawiera importera, CMS ani panelu.',
        'Nie zmieniaj data-content-id przy edycji tekstu; przy dodaniu elementu nadaj mu nowy identyfikator unikalny na danej stronie.',
        'Zmiany struktury, nowych sekcji i kolejności opisz w UWAGACH. Wiersze wspólne wystarczy wypełnić raz.',
        'Odeślij kopię .xlsx pod nową nazwą. Generator chroni arkusz z wpisami w F/G przed nadpisaniem.',
        'Regeneracja: python3 tools/make_content_template.py. Kontrola: python3 tools/make_content_template.py --check.',
        'Stare T001–T109 dotyczą wejścia sprzed przebudowy (e92207f). Ich zastosowanie opisano w docs/source-mapping.md.',
        'Demo pozostaje noindex,nofollow. Robots, SVG, skrypty, style i dekoracje aria-hidden nie są eksportowane.',
    ]
    for i, value in enumerate(instructions, 1):
        c = info.cell(i, 1, value)
        c.alignment = Alignment(wrap_text=True, vertical='top')
        info.row_dimensions[i].height = 34
    info['A1'].font = Font(bold=True, size=15, color='1F3D3A')
    ws = wb.create_sheet('Teksty')
    ws.append(['ID', 'Strona (plik)', 'Sekcja', 'Rodzaj elementu', 'OBECNY TEKST', 'NOWY TEKST (wypełnij)', 'UWAGI', 'Kontekst / element HTML', 'Pole / atrybut'])
    for row in rows:
        ws.append(row.values())
    for i, width in enumerate([40, 30, 28, 28, 80, 80, 45, 65, 16], 1):
        ws.column_dimensions[get_column_letter(i)].width = width
    for cell in ws[1]:
        cell.font = Font(bold=True, color='FAF7F2')
        cell.fill = PatternFill('solid', fgColor='1F3D3A')
        cell.alignment = Alignment(wrap_text=True, vertical='center')
    ws.row_dimensions[1].height = 32
    for row in ws.iter_rows(min_row=2):
        for cell in row:
            cell.alignment = Alignment(wrap_text=True, vertical='top')
            if isinstance(cell.value, str):
                cell.data_type = 's'
        row[5].fill = PatternFill('solid', fgColor='A8D48E')
        row[6].fill = PatternFill('solid', fgColor='7DB9E8')
    ws.freeze_panes = 'F2'
    ws.auto_filter.ref = ws.dimensions
    output.parent.mkdir(parents=True, exist_ok=True)
    wb.save(output)
    return len(rows)


def check(rows, output=OUT):
    assert output.is_file(), f'Brak wzorca {output}; najpierw uruchom generator.'
    assert len({r.id for r in rows}) == len(rows), 'ID muszą być unikalne'
    assert {r.page for r in rows} == set(PAGES) | {SHARED}, 'Wymagane wszystkie 9 stron i blok wspólny'
    reference = None
    for page in PAGES:
        text = (ROOT / page).read_text()
        doc, selected = Document(text), extract(page, text)
        chrome = [chrome_key(r) for r in selected if r.section in CHROME]
        reference = reference or chrome  # index.html idzie pierwszy i wyznacza wzorzec
        assert chrome == reference, (page, 'Menu lub stopka różni się od index.html')
        for tag, attribute in [('title', 'text'), ('h1', 'text')]:
            nodes = [n for n in doc.nodes if n.tag == tag]
            assert len(nodes) == 1, (page, tag)
            assert any(r.attribute == attribute and r.text == nodes[0].text() for r in selected)
        assert sum(r.kind == 'Opis strony (meta description)' for r in selected) == 1
        links = [n for n in doc.nodes if n.tag == 'a' and not n.hidden()]
        assert sum(r.attribute == 'href' for r in selected) == len(links)
        for node in doc.nodes:
            if node.tag == 'p' and not node.hidden():
                assert any(r.attribute == 'text' and r.text == node.text() for r in selected), (page, 'Niepełny akapit', node.text())
        assert all(r.text not in {'→', 'USUŃ', 'MTQ'} for r in selected)
        assert not [r for r in rows if r.page == page and r.section in CHROME], (page, 'Zdublowana stopka/menu')
    # Focused extraction regressions: inline content, hidden void tags, SVG,
    # duplicate CTA, lists, source placeholder, every internal link.
    fixture = '''<main data-section="Test"><img aria-hidden="true" alt="DEKORACJA"><p data-content-id="a">Pełny <strong>akapit</strong> i <a href="index.html#kontakt">link</a>.</p><svg><text>SVG</text></svg><p data-content-id="b">Następny &lt;placeholder&gt;.</p><ul><li>Pierwszy<ul><li>Drugi</li></ul></li></ul><script>SKRYPT</script><style>STYL</style><span aria-hidden="true">OZDOBNIK</span><a data-content-id="c" href="coaching.html">Więcej</a><a data-content-id="d" href="mtq-plus.html">Więcej</a></main>'''
    sample = extract('fixture.html', fixture)
    texts = [r.text for r in sample if r.attribute == 'text']
    assert texts == ['Pełny akapit i link.', 'Następny <placeholder>.', 'Pierwszy', 'Drugi', 'Więcej', 'Więcej'], texts
    assert [r.text for r in sample if r.attribute == 'href'] == ['index.html#kontakt', 'coaching.html', 'mtq-plus.html']
    assert len({r.id for r in sample}) == len(sample)
    assert extract('other.html', fixture)[0].id != sample[0].id
    assert extract('inline.html', '<p>Opis <strong>ważny </strong>oraz<strong> istotny</strong>.</p>')[0].text == 'Opis ważny oraz istotny.'
    if output.is_file():
        wb = load_workbook(output, read_only=True)
        actual = list(wb['Teksty'].iter_rows(min_row=2, values_only=True))
        assert len(actual) == len(rows), 'Wzorzec nieaktualny: uruchom generator'
        for saved, row in zip(actual, rows):
            expected = row.values()
            for col in [0, 1, 2, 3, 4, 7, 8]:
                assert (saved[col] or '') == expected[col], (row.id, 'Wzorzec nieaktualny', col)
        wb.close()
    shared = sum(r.page == SHARED for r in rows)
    print(f'OK — {len(rows)} unikalnych wierszy ({shared} wspólnych dla menu i stopki); 9 stron; '
          'pełne akapity, linki, listy, meta, alt; regresje ekstrakcji.')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true')
    parser.add_argument('--output', type=Path, default=OUT)
    args = parser.parse_args()
    content = extract_site()
    if args.check:
        check(content, args.output)
    else:
        print(f'{args.output}: {build(content, args.output)} wierszy')
