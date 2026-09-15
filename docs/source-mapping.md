# Mapowanie źródeł — issue #1

Punkt odniesienia: `e92207f:index.html` oraz generator z tego commitu.
Odtworzono starą ekstrakcję i porównano wszystkie **109 ID i wartości D**
z wypełnionym arkuszem. Są identyczne. Nie przenumerowano wejścia przed
zastosowaniem decyzji. Kolejność nowych kart nie służyła jako klucz.

Pierwszeństwo: decyzje z issue → Excel dla strony głównej → brief dla opisów
i instrukcji wizualnych → strategia. `data-source-id` zachowuje pochodzenie
T001–T109, a `data-content-id` służy nowemu eksportowi wszystkich stron.

Jawne korekty: MTQ Plus (również skrót MTQ w T001 i liście wykształcenia),
angielskie rozwinięcia RAPID i cennik z decyzji właściciela. Nie zmieniano
biografii, twierdzeń zdrowotnych/psychometrycznych ani czasu i zakresu usług.
Nagłówek i opis strony głównej pochodzą z T002/T001 z powyższą korektą nazwy.

## Instrukcje strukturalne G

Wypełniono i zastosowano 16 komórek:

| ID | Wykonanie |
| --- | --- |
| T020 | Całe O zmianie nad O mnie, bez zwijania i przycisku „czytaj dalej”. |
| T029 | Dwie karty Moja/Twoja droga z krótkimi wstępami i pełnymi podstronami. |
| T032 | Moja droga → `moja-droga.html`, wspólny banner i nowa fotografia hero. |
| T035 | Twoja droga → `twoja-droga.html`, wspólny banner i nowa fotografia hero. |
| T038 | Warsztaty i szkolenia na pozycji 6. |
| T040 | `warsztaty-i-szkolenia.html`, pełny opis i końcowe CTA. |
| T041 | Interwencja kryzysowa na pozycji 2. |
| T043 | `interwencja-kryzysowa.html`, pełny opis i końcowe CTA. |
| T044 | Coaching na pozycji 1. |
| T046 | `coaching.html`, pełny opis i końcowe CTA. |
| T047 | Terapia dźwiękiem na pozycji 5. |
| T049 | `terapia-dzwiekiem.html`, pełny opis i końcowe CTA. |
| T050 | MTQ Plus na pozycji 4. |
| T052 | `mtq-plus.html`, pełny opis i końcowe CTA. |
| T053 | PRISM Brain Mapping na pozycji 3. |
| T055 | `prism-brain-mapping.html`, pełny opis i końcowe CTA. |

Każde nowe CTA na podstronie kieruje do `index.html#kontakt`. Istniejące CTA
na stronie głównej zachowują `#kontakt`, `#oferta` i dokładny adres LinkedIn.

## Pełne treści briefu

`tools/check_source_materials.py` wiąże 131 bloków tekstowych PDF z plikami
HTML. Numery bloków pochodzą z PyMuPDF 1.28.2 i są chronione hashem PDF.
`data-brief-block` ułatwia odszukanie akapitów w HTML. Kontrola normalizuje
odstępy i numerację list (przeniesioną do HTML), zachowując słowa i kolejność.
Od issue #6 pomija 19 bloków i wiersze T022, T031, T035, T039, T045, które
zastąpił arkusz tekstów właścicielki ([HANDOFF](../HANDOFF.md)). Ten arkusz
usunął też cennik.

| Strona | Strony briefu | Zakres |
| --- | --- | --- |
| index.html | 7 | Sześć pełnych akapitów O zmianie; O mnie z nadrzędnego Excela |
| moja-droga.html | 8–9 | Historia, wykształcenie, wydarzenia, doświadczenie, część prywatna i miejsce pracy |
| twoja-droga.html | 9–10 | Zmiana, sposoby wsparcia, możliwe efekty |
| coaching.html | 10–11 | ICC, proces, korzyści, standardy, 90 minut / co dwa tygodnie |
| interwencja-kryzysowa.html | 11–13 | Kontakt, definicja, RAPID, etapy, certyfikat, lista IPTK |
| prism-brain-mapping.html | 13–15 | Doświadczenie, badanie, interpretacja, lista praktyków; mapę z briefu usunięto (karta 1931) |
| mtq-plus.html | 15–16 | Doświadczenie, cztery obszary / osiem wymiarów, omówienie |
| terapia-dzwiekiem.html | 16–18 | Pełny masaż, przebieg, metoda Petera Hessa, zaproszenie |
| warsztaty-i-szkolenia.html | 18–19 | Opis, cennik, tematy, programy dla kobiet, sposób pracy i dopasowanie |

Zielone etykiety i żółte komentarze są instrukcjami układu. Polecenia dodania
przycisku wykonano jako CTA. Placeholdery we właściwym tekście zostały do
issue #6, w którym arkusz właścicielki je zastąpił lub usunął: pytania
o wykształcenie i wydarzenia, wielokropki zamiast lat/liczb, zasięg akcji,
a także `<tu wpisać firmy, w których pracowałaś i z którymi
współpracowałaś>` (w HTML `&lt;` / `&gt;`). Zachowano przypisanie cytatu Franklowi,
oboczność terapia/masaż i certyfikat `KK/95830225/2024`.

## Oryginały i zasoby

Sumy pięciu wejść zapisano w [source-hashes.json](source-hashes.json). Materiały
w `Wytyczne/` są identyczne bajtowo z pięcioma załącznikami Super Jirki
wskazanymi przy uruchomieniu. Nie zmieniono ich. Katalog jest ignorowany
przez Git i niedostępny przez lokalny serwer demo. Nowy `teksty-strony.xlsx`
w katalogu głównym jest oddzielnym eksportem, bez wpisów F/G.

Hero strony głównej, Mojej drogi i Twojej drogi: pełne `5G5A3573_pp.jpg`
(1659 × 1476), warianty WebP 640/1000/1400 px. Pozostałe podstrony mają własne
hero (niżej). O mnie: `5G5A3539_pp.jpg` (3265 × 4898), WebP 480/800/1100 px. Warianty
zachowują proporcje. Kontakt: `assets/portrait-contact.jpg`, identyczny
z `e92207f`; porównanie wymiarów w [QA.md](QA.md).

Przykładową mapę PRISM z briefu (figura z podpisem `prismbrainmapping.pl`
pod opisem badania) usunięto na prośbę właścicielki w karcie 1931. Razem z nią
zniknęły `assets/mapa-prism-brain-mapping.png` i `.webp` oraz styl `.prism-map`.
Koło PRISM pokazuje teraz tylko hero (niżej). Dekoracja `prism-brain.webp`
nie jest używana.

Hero PRISM Brain Mapping (issue #5) to puste koło z `6_Puste_Koło_PRISM.pdf`
od właścicielki, SHA-256
`1f27f9a49ad32ca44bfeba4e9a9ae50109b78768d15bb5012bf4c46e272981c0`.
PDF wyrenderowano poleceniem `pdftoppm -r 400` (4678 × 3307 px) i wycięto kwadrat
2400 × 2400 px ze środkiem koła w punkcie (1898, 1748). Piksele dalej niż 1113 px
od środka zamieniono na biel. Ten promień leży w pustym pierścieniu między
etykietami (do 1098 px) a listami przymiotników i paskami (od 1128 px). Zostaje
samo koło z ośmioma etykietami na białym tle, bez nagłówka, legendy i tabel.
Grafiki nie edytowano. Warianty `assets/hero-prism-640/1000/1400.webp` (WebP q90;
36, 64 i 101 KB) są kwadratowe, a HTML ma `width`/`height` 1000 × 1000.
Zaokrąglony róg obrazu nie ucina koła przy szerokości okna od 300 do 1600 px;
najmniej miejsca jest przy 761 px (promień 64 px, obraz 278 px).
PDF nie trafia do repozytorium.

Hero MTQ Plus (issue #4) to logo `4.png` od właścicielki (PNG 500 × 500 px
z paletą i przezroczystym tłem), SHA-256
`e0db831cd9f46a25a5cf77feb6e7d94f77b13130c6844a8b6636e53d0a47f155`.
Pod przezroczystymi pikselami zapisano kolor (71, 112, 76), więc konwersja bez
kanału alfa daje zielone tło. Logo nałożono na biel (Pillow `alpha_composite`)
bez skalowania, kadrowania i edycji; na przezroczystym tle przez literę M
przechodziłaby linia ramki `.hero-media::after`. `assets/hero-mtq-plus.webp`
to bezstratny WebP (5 KB), zgodny piksel w piksel z nałożeniem; stratny WebP
zmieniał kolory krawędzi liter. HTML ma jeden wariant `500w` i `width`/`height`
500 × 500. Napis zajmuje x 8–491 i y 194–303 px, więc zaokrąglony róg nie ucina
liter przy szerokości okna od 300 do 1600 px; najmniej miejsca jest przy 761 px
(109 px pod napisem, promień 64 px). Na ekranach 2× logo jest miękkie, bo plik
ma tylko 500 px (karta `next_steps` 1925). PNG nie trafia do repozytorium.

Hero Coachingu, Interwencji kryzysowej, Terapii dźwiękiem oraz Warsztatów
i szkoleń (issue #3) to zdjęcia wskazane przez właścicielkę w sekcji WYMIANA
ZDJĘĆ dokumentu „Kasia Chałas strona uwagi”. Kadr podano w pikselach oryginału
(lewy, górny – prawy, dolny). Wycięto go bez retuszu i wyostrzania, przeskalowano
filtrem Lanczos (Pillow 9.4) i zapisano jako WebP q85, `method=6`. Oryginały mają
profil sRGB IEC61966-2-1, więc WebP bez profilu ICC zachowuje kolory. EXIF
nie jest kopiowany.

| Podstrona | Źródło i SHA-256 | Kadr | W kadrze |
| --- | --- | --- | --- |
| coaching.html | `5G5A3595_pp.jpg` (3266 × 4898), `7ae141396ff2b055d937cbd29be18d466ea82cb56f45d5f8ee779f77ca456986` | 116, 250 – 3266, 3050: 3150 × 2800, 9:8 | Włosy od y ≈ 400, cała twarz i dłoń przy brodzie z bransoletkami. Druga dłoń leży na oparciu krzesła (y ≈ 3150–3870) pod kadrem; dolna krawędź przecina rękawy 100 px nad jej bransoletką. |
| interwencja-kryzysowa.html | `5G5A3840_pp.jpg` (4898 × 3265), `44355512148410654aa05630a6aff7c6a4e0575cc20130c2685a0cc96a5a52a6` | 369, 0 – 4041, 3264: 3672 × 3264, 9:8 | Włosy od y ≈ 170, twarz, dłoń przy policzku z bransoletkami, druga dłoń z zegarkiem i oparcie krzesła. Szczebelki pod oparciem ucina już oryginał. |
| terapia-dzwiekiem.html | `5G5A3696_pp.jpg` (4898 × 3265), `0554ed9cd6a4c291e5e14040ee2b6404f5234fcbcc55eb2c93d92cf5257cde59` | 1880, 0 – 4736, 3264: 2856 × 3264, 7:8 | Cała postać, pałka, misa w dłoniach i trzy misy na podłodze z czterema filcowymi podkładkami (x 2075–4545, y 185–3230). Zapas: 195 px z lewej, 191 px z prawej, 185 px u góry i ok. 34 px na dole, gdzie kończy się zdjęcie. Usunięto 1880 px białego tła z lewej i 162 px z prawej. |
| warsztaty-i-szkolenia.html | `5G5A3436_pp.jpg` (3265 × 4898), `2c27fb93206b6945e7f3e245f8c676f3c42f2cf3d98933aaca72bd36c64e3b58` | 175, 515 – 2875, 2915: 2700 × 2400, 9:8 | Włosy od y ≈ 640, twarz, kołnierz i ramiona do wysokości piersi. Dłoń w kieszeni (y ≈ 3900–4250) leży pod kadrem; krawędzie nie przecinają dłoni. |

Warianty `assets/hero-coaching-*`, `hero-interwencja-*` i `hero-warsztaty-*`
mają 640 × 569, 1000 × 889 i 1400 × 1244 px, a `hero-terapia-*` 640 × 731,
1000 × 1143 i 1400 × 1600 px. Pliki 640/1000/1400 ważą: Coaching 23/47/90 KB,
Interwencja 39/75/132 KB, Terapia 54/107/176 KB, Warsztaty 14/30/52 KB.
HTML ma `width`/`height` wariantu 1000 px. Alt Terapii dźwiękiem to „Katarzyna
Chałas z misami dźwiękowymi”; trzy pozostałe podstrony zachowują „Katarzyna
Chałas - coach”. Objęcie drugiej dłoni (Coaching, Warsztaty) wymagałoby
pionowego kadru ok. 8:9 lub 6:7 zamiast 9:8, więc zostaje ona poza kadrem.
JPG nie trafiają do repozytorium.
Warunki fontów: [assets/fonts/README.md](../assets/fonts/README.md).

## Stare ID → wdrożony HTML

45 wpisów F, w tym 16 usunięć; pozostałe 64 puste F zachowują dotychczasową
treść, z jawnymi wyjątkami powyżej. T023/T024 są podzielone na pełne akapity,
T018 na cytat i podpis, a T088 na akapit oraz semantyczny cennik (usunięty
w issue #6).

| ID wejścia | Decyzja F | Cel w index.html |
| --- | --- | --- |
| T001 | Nowy tekst | `[data-source-id="T001"]` |
| T002 | Nowy tekst | `[data-source-id="T002"]` |
| T003 | Bez zmiany tekstu | `a.skip-link` → `#main-content` |
| T004 | Bez zmiany tekstu | `[data-source-id="T004"]` |
| T005 | Nowy tekst | `[data-source-id="T005"]` |
| T006 | Bez zmiany tekstu | `[data-source-id="T006"]` → `#omnie` |
| T007 | Bez zmiany tekstu | `[data-source-id="T007"]` → `#oferta` |
| T008 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T009 | Bez zmiany tekstu | `[data-source-id="T009"]` → `#biznes` |
| T010 | Bez zmiany tekstu | `[data-source-id="T010"]` → `#kontakt` |
| T011 | Bez zmiany tekstu | `[data-source-id="T011"]` → `#kontakt` |
| T012 | Nowy tekst | `[data-source-id="T012"]` |
| T013 | Nowy tekst | `[data-source-id="T013"]` |
| T014 | Nowy tekst | `[data-source-id="T014"]` |
| T015 | Nowy tekst | `[data-source-id="T015"]` |
| T016 | Bez zmiany tekstu | `[data-source-id="T016"]` → `#kontakt` |
| T017 | Bez zmiany tekstu | `[data-source-id="T017"]` → `#oferta` |
| T018 | Nowy tekst | `[data-source-id="T018"]` |
| T019 | Nowy tekst | `[data-source-id="T019"]` |
| T020 | Bez zmiany tekstu | `[data-source-id="T020"]` |
| T021 | Bez zmiany tekstu | `[data-source-id="T021"]` |
| T022 | Nowy tekst | `[data-source-id="T022"]` |
| T023 | Nowy tekst | `[data-source-id="T023"]` |
| T024 | Nowy tekst | `[data-source-id="T024"]` |
| T025 | Bez zmiany tekstu | `[data-source-id="T025"]` |
| T026 | Bez zmiany tekstu | `[data-source-id="T026"]` |
| T027 | Bez zmiany tekstu | `[data-source-id="T027"]` |
| T028 | Bez zmiany tekstu | `[data-source-id="T028"]` |
| T029 | Bez zmiany tekstu | `[data-source-id="T029"]` |
| T030 | Bez zmiany tekstu | `[data-source-id="T030"]` |
| T031 | Nowy tekst | `[data-source-id="T031"]` |
| T032 | Bez zmiany tekstu | `[data-source-id="T032"]` → `moja-droga.html` |
| T033 | Bez zmiany tekstu | `[data-source-id="T033"]` |
| T034 | Bez zmiany tekstu | `[data-source-id="T034"]` |
| T035 | Nowy tekst | `[data-source-id="T035"]` |
| T036 | Bez zmiany tekstu | `[data-source-id="T036"]` → `twoja-droga.html` |
| T037 | Bez zmiany tekstu | `[data-source-id="T037"]` |
| T038 | Nowy tekst | `[data-source-id="T038"]` |
| T039 | Nowy tekst | `[data-source-id="T039"]` |
| T040 | Bez zmiany tekstu | `[data-source-id="T040"]` → `warsztaty-i-szkolenia.html` |
| T041 | Nowy tekst | `[data-source-id="T041"]` |
| T042 | Nowy tekst | `[data-source-id="T042"]` |
| T043 | Bez zmiany tekstu | `[data-source-id="T043"]` → `interwencja-kryzysowa.html` |
| T044 | Bez zmiany tekstu | `[data-source-id="T044"]` |
| T045 | Nowy tekst | `[data-source-id="T045"]` |
| T046 | Bez zmiany tekstu | `[data-source-id="T046"]` → `coaching.html` |
| T047 | Bez zmiany tekstu | `[data-source-id="T047"]` |
| T048 | Nowy tekst | `[data-source-id="T048"]` |
| T049 | Bez zmiany tekstu | `[data-source-id="T049"]` → `terapia-dzwiekiem.html` |
| T050 | Bez zmiany tekstu | `[data-source-id="T050"]` |
| T051 | Nowy tekst | `[data-source-id="T051"]` |
| T052 | Bez zmiany tekstu | `[data-source-id="T052"]` → `mtq-plus.html` |
| T053 | Bez zmiany tekstu | `[data-source-id="T053"]` |
| T054 | Nowy tekst | `[data-source-id="T054"]` |
| T055 | Bez zmiany tekstu | `[data-source-id="T055"]` → `prism-brain-mapping.html` |
| T056 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T057 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T058 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T059 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T060 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T061 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T062 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T063 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T064 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T065 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T066 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T067 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T068 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T069 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T070 | Nowy tekst | `[data-source-id="T070"]` |
| T071 | Bez zmiany tekstu | `[data-source-id="T071"]` |
| T072 | Bez zmiany tekstu | `[data-source-id="T072"]` |
| T073 | Bez zmiany tekstu | `[data-source-id="T073"]` |
| T074 | Bez zmiany tekstu | `[data-source-id="T074"]` |
| T075 | Bez zmiany tekstu | `[data-source-id="T075"]` |
| T076 | Bez zmiany tekstu | `[data-source-id="T076"]` |
| T077 | Bez zmiany tekstu | `[data-source-id="T077"]` |
| T078 | Bez zmiany tekstu | `[data-source-id="T078"]` |
| T079 | Nowy tekst | `[data-source-id="T079"]` |
| T080 | Bez zmiany tekstu | `[data-source-id="T080"]` |
| T081 | Bez zmiany tekstu | `[data-source-id="T081"]` |
| T082 | Bez zmiany tekstu | `[data-source-id="T082"]` |
| T083 | Bez zmiany tekstu | `[data-source-id="T083"]` |
| T084 | Bez zmiany tekstu | `[data-source-id="T084"]` |
| T085 | Nowy tekst | `[data-source-id="T085"]` |
| T086 | Bez zmiany tekstu | `[data-source-id="T086"]` |
| T087 | Bez zmiany tekstu | `[data-source-id="T087"]` |
| T088 | Nowy tekst | `[data-source-id="T088"]`; `.pricing` usunięty w issue #6 |
| T089 | Bez zmiany tekstu | `[data-source-id="T090"]` — `href` LinkedIn |
| T090 | Bez zmiany tekstu | `[data-source-id="T090"]` → `https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/` |
| T091 | Bez zmiany tekstu | `[data-source-id="T092"]` — `href` LinkedIn |
| T092 | Bez zmiany tekstu | `[data-source-id="T092"]` → `https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/` |
| T093 | Bez zmiany tekstu | `[data-source-id="T094"]` — `href` LinkedIn |
| T094 | Bez zmiany tekstu | `[data-source-id="T094"]` → `https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/` |
| T095 | Bez zmiany tekstu | `[data-source-id="T095"]` |
| T096 | Nowy tekst | `[data-source-id="T096"]` |
| T097 | Bez zmiany tekstu | `[data-source-id="T097"]` |
| T098 | Nowy tekst | `[data-source-id="T098"]` |
| T099 | Bez zmiany tekstu | `[data-source-id="T099"]` |
| T100 | Bez zmiany tekstu | `[data-source-id="T100"]` → `#omnie` |
| T101 | Bez zmiany tekstu | `[data-source-id="T101"]` → `#oferta` |
| T102 | USUŃ | Usunięto wraz z sekcją / odnośnikiem Narzędzia |
| T103 | Bez zmiany tekstu | `[data-source-id="T103"]` → `#biznes` |
| T104 | Bez zmiany tekstu | `[data-source-id="T104"]` → `#kontakt` |
| T105 | Bez zmiany tekstu | `[data-source-id="T105"]` |
| T106 | Bez zmiany tekstu | `[data-source-id="T107"]` — `href` LinkedIn |
| T107 | Bez zmiany tekstu | `[data-source-id="T107"]` → `https://www.linkedin.com/in/katarzyna-cha%C5%82as-747831b8/` |
| T108 | Bez zmiany tekstu | `[data-source-id="T108"]` |
| T109 | Nowy tekst | `[data-source-id="T109"]` |
