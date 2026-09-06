#!/usr/bin/env python3
"""Static acceptance checks. No server, private inputs or browser required."""
from pathlib import Path
from urllib.parse import unquote, urlsplit
import re
from make_content_template import Document, ROOT, PAGES, extract_site

PRICES = [('Sesje coachingowe', '400–600 zł'), ('Interwencja kryzysowa', '250 zł'), ('Masaż dźwiękiem według metody Petera Hessa', '300 zł'), ('PRISM Brain Mapping', '1392 zł'), ('MTQ Plus', 'do uzupełnienia'), ('Warsztaty i szkolenia', 'ustalenia indywidualne')]
LINKEDIN = 'https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/'


def check():
    docs = {page: Document((ROOT / page).read_text()) for page in PAGES}
    count = 0
    for page, doc in docs.items():
        nodes = doc.nodes
        ids = [n.attrs['id'] for n in nodes if 'id' in n.attrs]
        keys = [n.attrs['data-content-id'] for n in nodes if 'data-content-id' in n.attrs]
        assert len(ids) == len(set(ids)), (page, 'Powtórzone id')
        assert len(keys) == len(set(keys)), (page, 'Powtórzone data-content-id')
        assert next(n for n in nodes if n.tag == 'html').attrs.get('lang') == 'pl'
        assert len([n for n in nodes if n.tag == 'h1']) == 1
        assert any(n.tag == 'meta' and n.attrs.get('name') == 'robots' and n.attrs.get('content') == 'noindex,nofollow' for n in nodes)
        assert any(n.tag == 'meta' and n.attrs.get('name') == 'viewport' and 'width=device-width' in n.attrs.get('content', '') for n in nodes)
        assert any(n.tag == 'meta' and n.attrs.get('name') == 'description' and n.attrs.get('content') for n in nodes)
        assert next(n for n in nodes if n.tag == 'title').text()
        headings = [int(n.tag[1]) for n in nodes if re.fullmatch(r'h[1-6]', n.tag)]
        assert all(b <= a + 1 for a, b in zip(headings, headings[1:])), (page, headings)
        text = doc.root.text()
        assert not re.search(r'\bMTQ\b(?!\s+Plus)', text), (page, 'Nazwa narzędzia: MTQ Plus')
        for forbidden in ['MTQPlus', 'Reflecitve', 'Prioritatization', 'Interwention', 'Dysposition', 'wpisane w excela', 'Dodać przycisk', 'USUŃ']:
            assert forbidden not in text, (page, forbidden)
        assert not any('narzedzia' in n.attrs.get('href', '') or n.attrs.get('id') == 'narzedzia' for n in nodes)
        assert any(n.tag == 'a' and n.attrs.get('href') == '#main-content' for n in nodes)
        assert any(n.tag == 'main' and n.attrs.get('id') == 'main-content' and n.attrs.get('tabindex') == '-1' for n in nodes)
        for node in nodes:
            if node.tag == 'img':
                assert node.attrs.get('alt'), (page, 'Brak alt')
                assert int(node.attrs.get('width', 0)) > 0 and int(node.attrs.get('height', 0)) > 0
            for attribute in ['href', 'src']:
                url = node.attrs.get(attribute)
                if not url:
                    continue
                parsed = urlsplit(url)
                if parsed.scheme:
                    assert parsed.scheme == 'https', (page, url)
                    if node.tag == 'a':
                        assert node.attrs.get('target') == '_blank' and set(node.attrs.get('rel', '').split()) >= {'noopener', 'noreferrer'}
                    continue
                target = unquote(parsed.path) or page
                assert (ROOT / target).is_file(), (page, 'Brak zasobu', url)
                if parsed.fragment:
                    assert target in docs, (page, url)
                    assert any(n.attrs.get('id') == unquote(parsed.fragment) for n in docs[target].nodes), (page, 'Brak kotwicy', url)
                count += 1
            for attr in ['srcset', 'imagesrcset']:
                if attr in node.attrs:
                    assert all((ROOT / part.strip().split()[0]).is_file() for part in node.attrs[attr].split(',')), (page, attr)
        hero = next(n for n in nodes if n.tag == 'img' and 'hero-' in n.attrs.get('src', ''))
        preload = next(n for n in nodes if n.tag == 'link' and n.attrs.get('as') == 'image')
        assert hero.attrs['srcset'] == preload.attrs['imagesrcset']
        assert hero.attrs['sizes'] == preload.attrs['imagesizes']
        assert (hero.attrs['width'], hero.attrs['height']) == ('1659', '1476')
        if page != 'index.html':
            ctas = [n for n in nodes if n.tag == 'a' and n.text().startswith('Umów konsultację')]
            assert len(ctas) == 2
            assert all(n.attrs['href'] == 'index.html#kontakt' for n in ctas)
            assert any(n.tag == 'a' and n.attrs.get('href') == 'index.html' and 'brand' in n.attrs.get('class', '') for n in nodes)
            for n in nodes:
                if n.tag == 'a' and any(a.tag == 'nav' for a in n.ancestors()):
                    assert n.attrs['href'].startswith('index.html#'), (page, n.attrs)
    home = docs['index.html']
    sections = [n.attrs.get('id') or n.attrs.get('class') for n in home.nodes if n.tag == 'section' and n.parent.tag == 'main']
    assert sections == ['hero', 'ozmianie', 'omnie', 'journey container', 'oferta', 'biznes', 'korzysci', 'kontakt'], sections
    offer = next(n for n in home.nodes if n.attrs.get('id') == 'oferta')
    titles = [n.text() for n in offer.walk() if n.tag == 'h3']
    assert titles == ['Coaching', 'Interwencja kryzysowa', 'PRISM Brain Mapping', 'MTQ Plus', 'Terapia dźwiękiem', 'Warsztaty i szkolenia']
    assert [n.attrs['href'] for n in offer.walk() if n.tag == 'a'] == ['coaching.html', 'interwencja-kryzysowa.html', 'prism-brain-mapping.html', 'mtq-plus.html', 'terapia-dzwiekiem.html', 'warsztaty-i-szkolenia.html']
    for page in ['index.html', 'warsztaty-i-szkolenia.html']:
        dl = next(n for n in docs[page].nodes if n.tag == 'dl')
        names = [n.text() for n in dl.walk() if n.tag == 'dt']
        prices = [n.text() for n in dl.walk() if n.tag == 'dd']
        assert list(zip(names, prices)) == PRICES, (page, names, prices)
    contact = next(n for n in home.nodes if n.attrs.get('id') == 'kontakt')
    assert sum(n.tag == 'a' and n.attrs.get('href') == LINKEDIN for n in contact.walk()) == 3
    for n in home.nodes:
        if n.tag == 'a' and n.text() == 'Umów konsultację' and not any(a.attrs.get('id') == 'kontakt' for a in n.ancestors()):
            assert n.attrs['href'] == '#kontakt'
    assert any(n.tag == 'a' and n.text() == 'Poznaj ofertę' and n.attrs['href'] == '#oferta' for n in home.nodes)
    assert '<tu wpisać firmy, w których pracowałaś i z którymi współpracowałaś>' in docs['moja-droga.html'].root.text()
    inter = docs['interwencja-kryzysowa.html'].root.text()
    assert 'KK/95830225/2024' in inter
    for phrase in ['Reflective listening', 'Assessment of needs', 'Prioritization', 'Intervention', 'Disposition']:
        assert phrase in inter
    assert any(n.attrs.get('href') == 'https://www.iptk.pl/listakonsultantow/' for n in docs['interwencja-kryzysowa.html'].nodes)
    assert any(n.attrs.get('href') == 'https://prismbrainmapping.pl/praktycy-prism/' for n in docs['prism-brain-mapping.html'].nodes)
    assert any(n.attrs.get('src') == 'assets/mapa-prism-brain-mapping.webp' for n in docs['prism-brain-mapping.html'].nodes)
    assert any(n.tag == 'figcaption' and 'prismbrainmapping.pl' in n.text() for n in docs['prism-brain-mapping.html'].nodes)
    css = (ROOT / 'styles.css').read_text()
    for url in re.findall(r'url\("([^\"]+)"\)', css):
        assert (ROOT / url).is_file(), url
    assert all(color in css for color in ['#7DB9E8', '#A8D48E', '#1F3D3A', '#FAF7F2'])
    assert 'Newsreader' not in css and 'Manrope' not in css and 'narzedzia' not in css
    assert 'prefers-reduced-motion' in css
    rows = extract_site()
    assert len(rows) == len({r.id for r in rows})
    print(f'OK — 9 stron, {count} lokalnych odnośników/zasobów, kotwice, meta, nagłówki, ceny, CTA, źródła, fotografie i {len(rows)} ID.')


if __name__ == '__main__':
    check()
