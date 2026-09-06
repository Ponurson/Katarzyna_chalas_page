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
Ceny są dodatkowo sprawdzane jako sześć par nazwa–wartość.

| Strona | Strony briefu | Zakres |
| --- | --- | --- |
| index.html | 7 | Sześć pełnych akapitów O zmianie; O mnie z nadrzędnego Excela |
| moja-droga.html | 8–9 | Historia, wykształcenie, wydarzenia, doświadczenie, część prywatna i miejsce pracy |
| twoja-droga.html | 9–10 | Zmiana, sposoby wsparcia, możliwe efekty |
| coaching.html | 10–11 | ICC, proces, korzyści, standardy, 90 minut / co dwa tygodnie |
| interwencja-kryzysowa.html | 11–13 | Kontakt, definicja, RAPID, etapy, certyfikat, lista IPTK |
| prism-brain-mapping.html | 13–15 | Doświadczenie, badanie, konkretna mapa, interpretacja, lista praktyków |
| mtq-plus.html | 15–16 | Doświadczenie, cztery obszary / osiem wymiarów, omówienie |
| terapia-dzwiekiem.html | 16–18 | Pełny masaż, przebieg, metoda Petera Hessa, zaproszenie |
| warsztaty-i-szkolenia.html | 18–19 | Opis, cennik, tematy, programy dla kobiet, sposób pracy i dopasowanie |

Zielone etykiety i żółte komentarze są instrukcjami układu. Polecenia dodania
przycisku wykonano jako CTA. Placeholdery we właściwym tekście pozostają:
pytania o wykształcenie i wydarzenia, wielokropki zamiast lat/liczb, zasięg
akcji, a także `<tu wpisać firmy, w których pracowałaś i z którymi
współpracowałaś>` (w HTML `&lt;` / `&gt;`). Zachowano przypisanie cytatu Franklowi,
oboczność terapia/masaż i certyfikat `KK/95830225/2024`.

## Oryginały i zasoby

Sumy pięciu wejść zapisano w [source-hashes.json](source-hashes.json). Materiały
w `Wytyczne/` są identyczne bajtowo z pięcioma załącznikami Super Jirki
wskazanymi przy uruchomieniu. Nie zmieniono ich. Katalog jest ignorowany
przez Git i niedostępny przez lokalny serwer demo. Nowy `teksty-strony.xlsx`
w katalogu głównym jest oddzielnym eksportem, bez wpisów F/G.

Hero: pełne `5G5A3573_pp.jpg` (1659 × 1476), warianty WebP 640/1000/1400 px.
O mnie: `5G5A3539_pp.jpg` (3265 × 4898), WebP 480/800/1100 px. Warianty
zachowują proporcje. Kontakt: `assets/portrait-contact.jpg`, identyczny
z `e92207f`; porównanie wymiarów w [QA.md](QA.md).

`assets/mapa-prism-brain-mapping.png` porównano bajtowo z
[obrazem wskazanym w briefie](https://prismbrainmapping.pl/wp-content/uploads/2020/07/mapa-prism-brain-mapping.png).
Witryna korzysta z lokalnego WebP (1726 × 1151), z podpisem
`prismbrainmapping.pl`. Dekoracja `prism-brain.webp` nie jest używana.
Warunki fontów: [assets/fonts/README.md](../assets/fonts/README.md).

## Stare ID → wdrożony HTML

45 wpisów F, w tym 16 usunięć; pozostałe 64 puste F zachowują dotychczasową
treść, z jawnymi wyjątkami powyżej. T023/T024 są podzielone na pełne akapity,
T018 na cytat i podpis, a T088 na akapit oraz semantyczny cennik.

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
| T088 | Nowy tekst | `[data-source-id="T088"]` + `.pricing` (nagłówek, zdanie, 6 par dt/dd) |
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
