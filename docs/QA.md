# Kontrola demo — 2026-09-06

To raport pierwotnej przebudowy. Późniejsze poprawki wyglądu, nowe proporcje
tekstu względem zdjęć i ponowna weryfikacja są opisane w
[raporcie zmian po review](review-2026-09-06.md).

Kontrola dotyczy dziewięciu plików HTML w gałęzi `feat/issue-1-brand-rebuild`.
Środowisko: Raspberry Pi, Chromium **149.0.7827.196**, Playwright **1.58.2**,
axe-core **4.11.1**, Python 3.11, openpyxl 3.0.9, PyMuPDF 1.28.2.
Przeglądarka i serwer działały lokalnie. Nie wykonano deploymentu.

## Wyniki

| Kontrola | Wynik |
| --- | --- |
| `npm run check` | PASS: 9 stron, 201 lokalnych odnośników/zasobów, kotwice, H1–H3, meta, CTA, ceny, grafiki; 418 unikalnych wierszy Excela |
| `python3 tools/make_content_template.py --check` | PASS: wszystkie strony, pełne akapity, listy, etykiety, href, title/description, alt; brak SVG, skryptów i dekoracji |
| `python tools/check_source_materials.py` z PyMuPDF | PASS: 5 hashy oryginałów, T001–T109, 45 wpisów F, 16 usunięć, mapowanie instrukcji G, 131 bloków briefu |
| Stary generator na `e92207f:index.html` | Wszystkie 109 wartości D zgodne z wejściowym Excelem; mapowanie przed zmianą kolejności |
| `npm run check:browser` | PASS: 45 widoków, 8 pełnych ścieżek strona główna → podstrona → kontakt |
| axe: WCAG 2 A/AA, 2.1 AA, 2.2 AA | 0 zgłoszonych naruszeń i 0 niejednoznacznych wyników w 45 widokach; nie jest to deklaracja pełnej certyfikacji WCAG |
| JavaScript, zdjęcia, CSS i fonty w przeglądarce | 0 błędów konsoli/pageerror, 0 nieudanych żądań i 0 odpowiedzi HTTP ≥ 400 dla zasobów witryny |
| HTML5 (`html5lib`) | 0 błędów parsowania na każdej z 9 stron |
| `node --check script.js`, `node --check tools/check_browser.cjs` | PASS |
| Ochrona Excela | Próba regeneracji wypełnionego wzorca odrzucona; hash pliku zachowany. Brak XLSX wykrywany przez `--check` |
| Oryginały / załączniki Super Jirki | Wszystkie 5 par identyczne bajtowo; źródła niezmienione |

`npm ci` odtwarza zależności zapisane w `package-lock.json`. Kontrolę źródeł
wykonano interpreterem `/tmp/kch-redesign/venv/bin/python`; instrukcja utworzenia
własnego środowiska jest w README. Serwowanie strony i testy statyczne nie
wymagają materiałów prywatnych.

## Widoki i kontrola wizualna

Każda z dziewięciu stron została otwarta bezpośrednio w każdym widoku:

| Widok CSS | Liczba stron | Układ, zasoby, klawiatura, axe |
| --- | --- | --- |
| 320 × 812 | 9 | PASS |
| 375 × 812 | 9 | PASS |
| 390 × 844 | 9 | PASS |
| 768 × 1024 | 9 | PASS |
| 1440 × 900 | 9 | PASS |

Zrzuty całych stron: `artifacts/browser/<nazwa-strony>-<szerokość>x<wysokość>.jpg`.
Raport maszynowy: `artifacts/browser/report.json`. Dodatkowe widoki hero,
O mnie, oferty, kontaktu i cennika są w tym samym katalogu. Artefakty są lokalne,
ignorowane w Git; niniejszy raport jest częścią repozytorium.

Obejrzano stronę główną w wymaganych czterech rozdzielczościach, jej widoki
hero/oferta/O mnie/kontakt/cennik oraz reprezentatywne treści podstron i bannery.
Zdjęcia zachowują proporcje, pełny tekst przewija się pionowo, CTA nie nakładają
się, cennik i listy mieszczą się w kolumnach. Na małych telefonach pełny tekst
hero i cytat powodują, że fotografia znajduje się poniżej pierwszego ekranu;
pozostaje częścią rozwiniętego bannera, bez ukrywania treści.

Dodatkowo sprawdzono stronę główną przy szerokościach 360, 430, 600, 700, 701,
760, 761, 900, 1080, 1081, 1120, 1200, 1280, 1600 i 1920 px — bez poziomego
przewijania. Szczególnie sprawdzono granice układów mobilnych i desktopowych.
Na desktopie rzeczywista wysokość fotografii O mnie wynosi ok. 71,5% wysokości
tekstu przy 1081 px i ok. 85% przy 1200–1920 px. Na telefonie i tablecie zdjęcie
jest w osobnym wierszu, bez rozciągania.

## Zdjęcie kontaktowe — proporcjonalne 60%

Punkt odniesienia odtworzono z `e92207f` i zmierzono tą samą przeglądarką,
po załadowaniu fontów. `assets/portrait-contact.jpg` jest identyczny z plikiem
w tym commicie. Wartości poniżej dotyczą **samego obrazu**, w pikselach CSS:

| Widok | Przed: szer. × wys. | Po: szer. × wys. | Proporcja obu wymiarów |
| --- | --- | --- | --- |
| 320 × 812 | 320 × 340 | 192 × 204 | 60% |
| 375 × 812 | 375 × 346,28 | 225 × 207,77 | 60% |
| 390 × 844 | 390 × 360,13 | 234 × 216,08 | 60% |
| 768 × 1024 | 307,19 × 532,55 | 184,31 × 319,52 | 60% |
| 1440 × 900 | 576 × 646,33 | 345,59 × 387,80 | 60% |

Różnice poniżej 0,02 px wynikają z zaokrągleń układu przeglądarki. Kontener
obrazu ma nadal minimum 340/420 px; nie skalowano całej sekcji ani jej treści.
CSS zachowuje kadrowanie `object-fit: cover; object-position: 55% 28%`.
Pomiary bazowe: `artifacts/browser/baseline-contact.json`.

## Nawigacja i dostępność

Sprawdzono pierwszy Tab i widoczny focus skip-linku, przeniesienie focusu na
własny `main`, otwieranie menu Enter/Spacją, aktualizację `aria-expanded` oraz
etykiety otwórz/zamknij, zamknięcie Escape z powrotem focusu, kliknięcie poza
menu, opuszczenie menu focusem, wybór linku oraz zmianę szerokości ekranu.

Sprawdzono powrót marką, menu i stopką do rzeczywistych sekcji strony głównej,
wszystkie osiem linków z kart oraz końcowe CTA podstron. Z `prefers-reduced-motion`
przewijanie jest natychmiastowe, a animacje i przejścia wyłączone. Bez JavaScript
treści, podstrony i rozwinięta nawigacja pozostają dostępne.

Dwa kontaktowe CTA przetestowano przez kliknięcie i przechwycenie docelowego
żądania w nowej karcie: dokładny adres LinkedIn zgodny z issue, `window.opener`
jest `null`. W testach tych tylko odpowiedź LinkedIn jest lokalnie podstawiona;
wszystkie zasoby demo są rzeczywiście ładowane przez serwer.

## Źródła zewnętrzne i fonty

Odczyt HTTP wykonany 2026-09-06:

| Adres | Wynik |
| --- | --- |
| [Lista IPTK](https://www.iptk.pl/listakonsultantow/) | 200 |
| [Praktycy PRISM](https://prismbrainmapping.pl/praktycy-prism/) | 200 |
| [Mapa PRISM](https://prismbrainmapping.pl/wp-content/uploads/2020/07/mapa-prism-brain-mapping.png) | 200; lokalny PNG identyczny bajtowo z pobranym plikiem |
| [Wskazany pakiet Allrounder](https://font.download/font/allrounder-antiqua-test) | 200; użyte WOFF identyczne z pobranym pakietem web |
| [Profil LinkedIn](https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/) | 999 — blokada automatycznego odczytu; poprawność celu i obsługi CTA sprawdzono oddzielnie |

Chrome DevTools potwierdza, że H1 rysuje prawdziwy
`AllrounderAntiquaTest-Regular`, a cytat prawdziwy
`AllrounderAntiquaTest-RegularItalic`. Znaków nieobecnych w wersji Test nie
usuwano: w tym środowisku rysuje je Liberation Serif jako systemowy fallback.
Montserrat zawiera polskie litery. [Dokumentacja fontów](../assets/fonts/README.md)
opisuje warunki oraz istniejącą kartę `next_steps` **1879** dotyczącą pełnego
fontu i uprawnień. Ten brak materiału nie został przedstawiony jako zakup licencji.

## Granice kontroli

Nie wykonano testów na fizycznym iPhonie/Androidzie, w Safari, Firefox ani
z czytnikiem ekranu. Automatyczne i wizualne kontrole dotyczą Chromium.
Nie potwierdzono zawartości profilu LinkedIn za blokadą 999 ani licencji
produkcyjnej Allrounder; nie zmieniono tych ustaleń samodzielnie.
Nie wykonano publikacji, merge do `main`, konfiguracji Pages ani indeksowania.

Podczas pełnej sekwencji browser QA temperatura wynosiła 57,85–62,80°C;
bieżące flagi zasilania/throttlingu były zerowe. Sprawdzano je przed każdą stroną.
