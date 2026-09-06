# Katarzyna Chałas — demo

Statyczny HTML/CSS/JavaScript: strona główna i osiem pełnych podstron zgodnie z
[issue #1](https://github.com/Ponurson/Katarzyna_chalas_page/issues/1).
Nie wymaga frameworka, kompilacji ani backendu. Każda strona ma
`noindex,nofollow`. Zakres wdrożenia i wyniki: [HANDOFF.md](HANDOFF.md),
[raport QA](docs/QA.md), [mapowanie źródeł](docs/source-mapping.md).

## Podgląd lokalny

```bash
python3 tools/serve_demo.py
```

Otwórz `http://127.0.0.1:8765`. Serwer wiąże się wyłącznie z loopback i udostępnia
dziewięć plików HTML, CSS, JS oraz `assets/`. Blokuje dokumenty wejściowe,
skoroszyt, narzędzia i `.git`. Dostępny jest też `--port 8767` lub `npm start`.
Po skopiowaniu samej witryny te same pliki działają na zwykłym serwerze statycznym;
trasy nie wymagają przepisywania adresów.

| Strona | Plik |
| --- | --- |
| Główna | `index.html` |
| Moja droga | `moja-droga.html` |
| Twoja droga | `twoja-droga.html` |
| Coaching | `coaching.html` |
| Interwencja kryzysowa | `interwencja-kryzysowa.html` |
| PRISM Brain Mapping | `prism-brain-mapping.html` |
| MTQ Plus | `mtq-plus.html` |
| Terapia dźwiękiem | `terapia-dzwiekiem.html` |
| Warsztaty i szkolenia | `warsztaty-i-szkolenia.html` |

## Teksty i Excel

`teksty-strony.xlsx` jest nowym, pustym wzorcem wygenerowanym z **wdrożonych
dziewięciu stron**. Nie jest plikiem wejściowym z katalogu `Wytyczne/`.

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python tools/make_content_template.py
python tools/make_content_template.py --check
```

Na tym hoście wystarcza też systemowy `python3` z zainstalowanym `openpyxl`.
Wzorzec ma 682 wiersze i kolumny: ID, strona, sekcja, rodzaj, obecny tekst (E),
nowy tekst (F), uwagi (G), kontekst HTML i pole/atrybut.

1. Wypełniaj F/G w kopii skoroszytu. **Puste F = bez zmiany; USUŃ = usunięcie
   elementu HTML**. W wierszu atrybutu, np. `href`, USUŃ oznacza usunięcie całego
   linku. Usunięcie tekstu nagłówka lub linku może wymagać opisania przebudowy w G.
2. ID ma postać `coaching:e044:text`: strona, trwały `data-content-id`, pole.
   Przykładowo ten sam przycisk na innej stronie ma inny ID. Kontekst podaje
   selektor, a dla linków także etykietę i adres. Zmiany stosuje się według tych
   pól, nigdy według samego „Więcej” lub numeru wiersza Excela.
3. Akapity są eksportowane w całości wraz z tekstem linków i wyróżnień; adresy
   linków mają osobne wiersze `href`. Listy, usługi i ceny mają osobne pozycje.
   Zmiana tekstu akapitu musi zachować jego linki i semantyczne formatowanie.
4. Wykonawca nanosi zmiany ręcznie w HTML. Projekt nie ma importera ani CMS-a.
   Przy edycji zachowuj `data-content-id`; nowym elementom nadawaj nowe ID,
   unikalne w obrębie pliku. Menu i stopki są jawnie obecne w każdym HTML.
5. Regeneruj wzorzec po zmianach. Generator odmówi nadpisania skoroszytu
   z wypełnionym F/G; użyj `--output teksty-strony-nowy-wzorzec.xlsx`.

Stare T001–T109 zostały zastosowane przed zmianą kolejności. Ich mapowanie
pozostaje w `data-source-id` oraz [dokumencie źródeł](docs/source-mapping.md).
`--check` sprawdza wszystkie strony, pełne akapity, adresy, unikalność ID,
pomijanie dekoracji i zgodność istniejącego XLSX z HTML; nie zapisuje plików.

## Weryfikacja

```bash
python3 tools/check_site.py
python3 tools/make_content_template.py --check
npm ci
npm run check:browser
```

Ostatnia komenda sama uruchamia lokalny serwer i Chromium, wykonuje kolejno
45 widoków, audyt axe, obsługę menu/klawiatury i osiem ścieżek oferta–kontakt.
Zrzuty i JSON trafiają do ignorowanego `artifacts/browser/`. Domyślnie korzysta
z `/usr/bin/chromium`, jeśli jest obecny; gdzie indziej z przeglądarki Playwright
(`npx playwright install chromium`). Można podać `CHROMIUM_PATH`.
Na Raspberry Pi skrypt monitoruje temperaturę i bieżące flagi zasilania oraz
odmawia startu przy niedawnym spadku napięcia. Pracuje jedną przeglądarką.

Opcjonalne porównanie prywatnych materiałów:

```bash
. .venv/bin/activate
python -m pip install -r tools/requirements-source-audit.txt
python tools/check_source_materials.py
# Albo: python tools/check_source_materials.py --source-dir /sciezka/do/materialow
```

Materiały nie są wymagane do podglądu ani zwykłych kontroli. Nie dodawaj ich do
Gita lub serwowanej witryny. SHA-256 oryginałów zapisano w
[source-hashes.json](docs/source-hashes.json).

## Fonty i publikacja

Pochodzenie, warunki i ograniczenie polskich glifów w Allrounder Test opisano w
[assets/fonts/README.md](assets/fonts/README.md). Pełny font z uprawnieniami jest
w istniejącej karcie `next_steps` **1879**, projekt 1753. Cena MTQ Plus oraz
placeholdery tekstowe pozostają zgodne z decyzjami właściciela.

Przebudowa jest opublikowana na GitHub Pages:
<https://ponurson.github.io/Katarzyna_chalas_page/>. Pages buduje z gałęzi `main`
i katalogu `/`, więc publikuje każdy push do `main`; nie ma workflow ani kroku
budowania. Adresy w `index.html` i podstronach są względne i działają pod
podkatalogiem `/Katarzyna_chalas_page/`. `404.html` jest serwowana przez Pages dla
złych adresów i jako jedyna używa adresów bezwzględnych z tym prefiksem.

Wszystkie strony nadal mają `noindex,nofollow`, więc wyszukiwarki nie indeksują
demo. Zdjęcie zgody na indeksowanie i własna domena to decyzje właścicielki.
