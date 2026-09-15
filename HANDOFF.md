# Handoff — issue #1

## Karty 1933 i 1934 — strzałki i wielkość fontu (2026-09-15)

Dokończono zmiany zatrzymane limitem poprzedniego agenta. Wszystkie rozmiary
Cormorant Infant zwiększono o 2 pt (2⅔ px CSS), z uwzględnieniem breakpointów,
marki, haseł i cytatu. Montserrat, w tym nagłówki sekcji Dla biznesu, zachował
rozmiary. Nagłówek „Jak mogę wesprzeć Ciebie i Twój zespół” używa Cormorant
Infant o wadze 530 — zmiana rodziny z Allrounder Antiqua wynika z karty 1879.
W tej poprawce zwiększono jego rozmiar tak jak pozostałych nagłówków Cormorant.

W ośmiu linkach powrotu znak ← zastąpiono SVG z `aria-hidden="true"`.
Przed poprawką DevTools pokazywało jeden glif systemowego Liberation Sans
obok tekstu Montserrat. Kontrola fontów przeglądarki obejmuje teraz także
`.back-link`, aby wykryć ponowny fallback. Dostępna nazwa to „Strona główna”,
cel linku pozostaje ten sam. Zregenerowano wzorzec Excel (368 wierszy).
Odstępy przy przyciskach hero na desktopie zmniejszono, aby większy tekst
nadal mieścił się na wysokości zdjęcia. Pomiar przeszedł dla 11 szerokości
od 1024 do 1920 px; 364 próbki tekstu przy 390/768/1440 px potwierdziły
przyrost o 2 pt tylko dla Cormorant Infant.

PASS: `npm run check`, `npm run check:browser` (45 widoków, osiem ścieżek,
axe, fonty bez fallbacku w nagłówkach i linkach powrotu), `git diff --check`.


Aktualizacja po review: monogram KC, ciemny nagłówek, wyrównane kolumny tekstu
i zdjęć, przywrócone tła i kafelki, Montserrat Bold w Dla biznesu, baner oraz
cennik. Szczegóły i pomiary laptopów/telefonów:
[raport zmian po review](docs/review-2026-09-06.md).
Poniżej zapis pierwotnego wdrożenia i późniejszej konfiguracji publikacji.

## Karta 1914 — zamknięte issue #1

Issue #1 było nadal otwarte z etykietą `ready-for-agent`, choć przebudowę wdrożono
(karta 1869) i opublikowano (`c0788bb`). 2026-09-15 zamknięto je jako ukończone
i zdjęto etykietę, żeby agent wybierający zadania po niej nie powtórzył przebudowy.
[Komentarz zamykający](https://github.com/Ponurson/Katarzyna_chalas_page/issues/1#issuecomment-5677266728)
wymienia zmiany, które zastąpiły część opisu (hero podstron, cennik, font, mapa
PRISM, publikacja). Opisu issue nie należy więc wdrażać ponownie. Przed zamknięciem
sprawdzono, że dziewięć stron na Pages zwraca 200 i ma `noindex,nofollow`.

Karta **1935** zakończona 2026-09-15: issues #3–#6 zamknięto po sprawdzeniu
implementacji i GitHub Pages; zdjęto etykiety `ready-for-agent`.

## Karta 1931 — usunięta mapa PRISM w treści

Zgodnie z kartą **1931** („Usuń tę grafikę”, zrzut ekranu telefonu
`IMG-20260915-WA0002.jpg`) z `prism-brain-mapping.html` usunięto przykładową mapę
PRISM spod akapitu e053. Zniknęła cała `figure.prism-map`: link do pełnego
rozmiaru (e056), obraz (e057) i podpis „Źródło: prismbrainmapping.pl” (e058, e059).
Po akapicie od razu jest H2 „Co pokazuje PRISM Brain Mapping?”. Pozostałe teksty
i hero z pustym kołem (#5) są bez zmian.

Usunięto też `assets/mapa-prism-brain-mapping.webp` (195 KB) i `.png` (1,6 MB),
których nic już nie używa, więc Pages przestaje je publikować, oraz styl
`.prism-map`. `tools/check_site.py` zamiast obecności mapy sprawdza, że podstrona
PRISM nie ma `figcaption` ani odwołania do `mapa-prism`. Na HTML sprzed zmiany
kontrola kończy się błędem. Zregenerowany `teksty-strony.xlsx` ma 368 wierszy
(373 − 5). Zniknęły tylko wiersze `prism-brain-mapping:e056:href`,
`e056:aria-label`, `e057:alt`, `e058:text` i `e059:href`. Pozostałe wiersze
i instrukcja są identyczne, a F/G puste. Usunięcie opisano
w [mapowaniu źródeł](docs/source-mapping.md); `docs/QA.md` to raport historyczny.
Issue #2 (zamiana tej mapy na puste koło z PDF-u) straciło aktualność.

PASS: `python3 tools/check_site.py` (200 lokalnych odnośników/zasobów, wcześniej
201), `python3 tools/make_content_template.py --check` (368 wierszy),
`tools/check_source_materials.py` (PyMuPDF 1.28.2 w tymczasowym venv; 112 bloków,
19 zastąpionych, jak przed zmianą) i `npm run check:browser` (45 widoków, axe,
brak błędów JS i zasobów, 61–66 °C). Na podstronie PRISM przy 390 × 844
i 1440 × 900 odstęp akapit e053 → H2 wynosi 48 px, jak w reszcie artykułu,
a strona nie przewija się poziomo.

## Karta 1879 — Cormorant Infant zamiast Allroundera

Zgodnie z odpowiedzią właścicielki w karcie **1879** („Niech zamieni Allroundera
na Cormorant Infant i dopasuje grubość fontu…”) nagłówki, marka, hasła i cytat
używają Cormorant Infant z Google Fonts (SIL OFL 1.1). Usunięto oba WOFF Allrounder
Antiqua Test i `Allrounder-NOTICE.txt`. Font nie wymaga zakupu licencji ani plików
od właścicielki. Montserrat jest bez zmian.

`assets/fonts/CormorantInfant-Variable.woff2` (43 KB) i
`CormorantInfant-Italic-Variable.woff2` (45 KB) to podzbiory fontów zmiennych
z google/fonts `3dd7884`. Obejmują łacinę z rozszerzeniami A i B, więc mają
`ĄĆĘŁŃÓŚŹŻąćęłńóśźż`. Preload na dziewięciu stronach wskazuje nowy plik prosty.

Wagę dobrano pomiarem. Miarą jest średnia grubość kreski (2 × pole / obwód
konturu) względem wysokości x, liczona na znakach tekstów szeryfowych strony.
Allrounderowi Regular odpowiada waga 529, a Italic 564. W CSS ustawiono
`--serif-weight: 530` i `--serif-italic-weight: 560`. Pozostałe miary dają
467–516 i 514–583; tabela jest w [dokumentacji fontów](assets/fonts/README.md).
Rozmiarów, odstępów liter i interlinii nie zmieniano. Wysokość x Cormoranta to
78 % Allroundera, więc przy tych samych rozmiarach nagłówki są optycznie mniejsze
i krótsze. H1 strony głównej przy 1440 px ma 2 wiersze zamiast 3, a H1
Interwencji kryzysowej 1 zamiast 2.

`tools/check_browser.cjs` oczekuje rodziny `"Cormorant Infant"` w H1. Przy 1440 px
odczytuje z DevTools (`CSS.getPlatformFontsForNode`) fonty, które narysowały H1–H3,
markę, hasła i cytat. Font systemowy wśród nich przerywa test. Próba z podstawionym
podzbiorem ASCII bez polskich liter kończy się błędem `index.html: brak glifów
Cormorant Infant system LiberationSerif,…`. DevTools podaje nazwę domyślnej
instancji pliku zmiennego (`CormorantInfant-Light`); wagę 530/560 ustawia CSS.

PASS: `python3 tools/check_site.py`, `python3 tools/make_content_template.py --check`
(373 wiersze; teksty bez zmian, więc wzorca nie regenerowano) i
`npm run check:browser` (45 widoków, axe, brak błędów JS i zasobów, 61–66 °C).
Na dziewięciu stronach tekst szeryfowy rysuje wyłącznie Cormorant Infant.
Na stronie głównej tekst hero od 1024 px i O mnie od 1081 px do 1920 px ma
wysokość zdjęć (proporcja 1,0000). Żadna strona nie przewija się poziomo przy
28 szerokościach od 300 do 1920 px. Porównano zrzuty przed i po przy 1440 × 900
i 390 × 844 (2×) oraz próbki wag 400–700.

Poza zakresem zgłoszono kartę `bugs` **1933**: strzałki „←” w linku powrotu
podstron nie ma w podzbiorze Montserrat, więc rysuje ją font systemowy.

## Issue #6 — teksty z wypełnionego arkusza właścicielki

Źródło to wzorzec `teksty-strony.xlsx` wypełniony przez właścicielkę, pobrany
z Google Drive (id `1J1P34PYw813n_r3la1kDh0pa8pEx8kxC`, SHA-256
`16da8752156dae73801d71e47e50ef64df3fa393640ed5e8a6ee120a83e4c0af`). Lokalnie
leży w `poprawki/teksty-zmiany.xlsx`; `poprawki/` jest ignorowany przez Git.
Arkusz ma 418 ID wzorca z `f963550` i wpisy F/G w 65 wierszach. Przed zmianą
kolumna E tych wierszy zgadzała się z HTML.

Wprowadzono 64 wiersze: 17 nowych tekstów dosłownie, z interpunkcją właścicielki
(także z usuniętymi kropkami), oraz 46 usunięć razem z pustymi kontenerami.
Usunięto cały cennik: `div.pricing` na stronie głównej i `section.article-pricing`
w Warsztatach. Z Warsztatów zniknęła też sekcja „Dla liderów, zespołów
i organizacji” z listą tematów. Z Mojej drogi zniknęły „Background prawniczy”,
nagłówek wydarzeń z listą i akapit o doświadczeniu z placeholderami. Zgodnie
z uwagą w G pod „Certyfikowana Coachka ICC Poland” jest nowy `li` `e081`
(kolejny wolny ID) o studiach w Akademii Leona Koźmińskiego. Wiersz
`prism-brain-mapping:e056:href` (puste koło zamiast mapy) należy do #2 i go
pominięto.

Usunięto nieużywane style `.pricing`, `.price-list`, `.article-pricing` i zrzut
`cennik` w `tools/check_browser.cjs`. Zamiast sześciu par cen `tools/check_site.py`
sprawdza, że żadna strona nie zawiera słów „cennik” ani „zł”. Pilnuje też braku
placeholderów w Mojej drodze i miejsca wersu o Koźmińskim pod ICC Poland.
Opcjonalny `tools/check_source_materials.py` pomija wiersze T022, T031, T035,
T039, T045 i 19 bloków briefu zastąpionych arkuszem. Zregenerowany
`teksty-strony.xlsx` ma 373 wiersze (418 − 46 + 1) i puste F/G; z instrukcji
usunięto zdanie o cenniku. Porównanie `extract_site()` przed zmianą i po niej:
zmieniły się tylko ID z arkusza i doszedł nowy `li`, a pozostałe 353 wiersze
są identyczne. Nowe teksty są równe kolumnie F po normalizacji odstępów.

PASS: `python3 tools/check_site.py`, `python3 tools/make_content_template.py --check`
(373 wiersze) i `npm run check:browser` (45 widoków, axe, brak błędów JS
i zasobów, brak poziomego przewijania). Przechodzi też
`tools/check_source_materials.py` (PyMuPDF 1.28.2 w tymczasowym venv;
112 bloków, 19 zastąpionych). Na zrzutach 390 × 844 i 1440 × 900 nie ma pustych
sekcji. W miejscach usunięć odstęp akapit → H2 wynosi 48 px, jak w reszcie
artykułu, a lista → akapit 32 px. Kontakt kończy się zwykłym dopełnieniem sekcji.
`noindex,nofollow` bez zmian.

Do potwierdzenia z właścicielką (nie blokuje, karta `next_steps` **1926**):
nowy akapit e084 w Warsztatach mówi o „kobietach i mężczyznach 55+”. Nagłówek
e083 „Focus na odporność psychiczną i wellbeing kobiet” i akapit e085 o kobietach
nie mają wpisów, więc zostały bez zmian. Bez wpisu zostały też nagłówek e088
„Szkolenie dopasowane do rzeczywistej potrzeby” i meta description z
„przywództwa”.

## Issue #3 — hero Coachingu, Interwencji kryzysowej, Terapii dźwiękiem i Warsztatów

Zgodnie z uwagami właścicielki (sekcja WYMIANA ZDJĘĆ) cztery podstrony mają
nowe zdjęcia w hero: `coaching.html` — `5G5A3595_pp.jpg`,
`interwencja-kryzysowa.html` — `5G5A3840_pp.jpg`, `terapia-dzwiekiem.html` —
`5G5A3696_pp.jpg`, `warsztaty-i-szkolenia.html` — `5G5A3436_pp.jpg`. Coaching,
Interwencja i Warsztaty mają kadr 9:8 jak dotychczasowe hero: cała głowa
z zapasem nad włosami i cała twarz. Dłonie przy twarzy są w całości, a krawędzie
nie przecinają żadnej dłoni. Druga dłoń (Coaching: na oparciu krzesła,
Warsztaty: w kieszeni) jest pod kadrem. Terapia dźwiękiem ma kadr 7:8: cała
postać, pałka i wszystkie misy z podkładkami, a z białego tła zostało ok. 190 px
zapasu z boków. Zdjęć nie retuszowano.

Warianty `assets/hero-{coaching,interwencja,terapia,warsztaty}-640/1000/1400.webp`
(WebP q85) przy 1400 px mają 90, 132, 176 i 52 KB. `img` i `preload` mają nowe
`src`/`srcset`, a `width`/`height` odpowiadają wariantowi 1000 px (1000 × 889,
Terapia 1000 × 1143). Alt Terapii dźwiękiem to „Katarzyna Chałas z misami
dźwiękowymi”, pozostałe są bez zmian. `tools/check_site.py` odczytuje wymiary
z nagłówków WebP zamiast słownika `HERO_SIZES`. Deskryptor `w` każdego wariantu
musi równać się szerokości pliku, a proporcje `width`/`height` proporcjom pliku
(tolerancja 0,005). W zregenerowanym `teksty-strony.xlsx` zmieniły się tylko
cztery wiersze `…:e046:alt` (ścieżka obrazu, alt Terapii). Kadry i SHA-256
opisano w [mapowaniu źródeł](docs/source-mapping.md). Hero strony głównej,
Mojej drogi i Twojej drogi są bez zmian. JPG nie są w repozytorium.

PASS: `python3 tools/check_site.py`, `python3 tools/make_content_template.py --check`
(418 wierszy, puste F/G) i `npm run check:browser` (45 widoków, axe, brak błędów
JS i zasobów). Kontrola odrzuca zmieniony `height` i zły deskryptor `w`. Przy 2×
dla 320, 390, 768 i 1440 px przeglądarka wybiera wariant o 2,4–3,6 px obrazu
na 1 px CSS; włosy, rzęsy i bransoletki są ostre. Zaokrąglony róg nie ucina
postaci, mis ani podkładek przy szerokości okna od 300 do 1600 px. Najmniej
miejsca jest przy 761 px: 16,5 px CSS do podkładki. Na trzech zdjęciach 9:8
róg nie sięga głowy, twarzy ani dłoni.

## Issue #4 — hero MTQ Plus

Zgodnie z uwagami właścicielki („logotyp badania MTQ Plus znajdujący się
w folderze”) zdjęcie w hero `mtq-plus.html` zastąpiono logo z `4.png`
(500 × 500 px). Przezroczyste tło zamieniono na białe; logo nie skalowano,
nie kadrowano i nie edytowano. `assets/hero-mtq-plus.webp` to bezstratny WebP
(5 KB). `img` i `preload` mają `src`/`srcset` z jednym wariantem `500w`,
`width`/`height` 500 × 500 i `alt` „Logo badania MTQ Plus”.
`tools/check_site.py` sprawdza wymiary hero MTQ Plus osobno. W zregenerowanym
`teksty-strony.xlsx` zmienił się tylko wiersz `mtq-plus:e046:alt` (alt i ścieżka
obrazu w kontekście). Konwersję i SHA-256 opisano w
[mapowaniu źródeł](docs/source-mapping.md). Hero pozostałych stron są bez zmian.
PNG nie jest w repozytorium.

PASS: `python3 tools/check_site.py`, `python3 tools/make_content_template.py --check`
(418 wierszy, puste F/G) i `npm run check:browser` (45 widoków, axe, brak błędów
JS i zasobów). Zrzuty przy 390 × 844 i 1440 × 900 (1× i 2×) pokazują całe logo
w proporcjach 1:1. Ramka leży pod nieprzezroczystym obrazem, a zaokrąglony róg
nie ucina liter przy szerokości okna od 300 do 1600 px. Litery zaczynają się
ok. 8 px od bocznych krawędzi pliku, więc prawie dotykają brzegów białego kwadratu.

Logo jest nieostre na ekranach 2×: przy 450 px CSS przeglądarka rozciąga 500 px
do 900 px. Krawędzie liter mają przejście 10–90 % szerokie na ok. 3,8 px
urządzenia, a wektorowy H1 obok 1,9 px. Karta `next_steps` **1925** prosi
o logo jako SVG albo PNG co najmniej 1000 × 1000 px.

## Issue #5 — hero PRISM Brain Mapping

Zgodnie z uwagami właścicielki („PUSTE KOŁO CZTERECH KOLORÓW”) zdjęcie w hero
`prism-brain-mapping.html` zastąpiono pustym kołem z `6_Puste_Koło_PRISM.pdf`.
Kadr zawiera samo koło z ośmioma etykietami na białym tle. Grafiki nie edytowano.
Kwadratowe `assets/hero-prism-640/1000/1400.webp` mają 36, 64 i 101 KB.
`img` i `preload` mają nowe `src`/`srcset`, `width`/`height` 1000 × 1000 i `alt`
„Puste koło PRISM Brain Mapping w czterech kolorach”. `tools/check_site.py`
sprawdza wymiary hero PRISM osobno. W zregenerowanym `teksty-strony.xlsx` zmienił
się tylko wiersz `prism-brain-mapping:e046:alt`. Render, SHA-256 i kadr opisano
w [mapowaniu źródeł](docs/source-mapping.md). Hero pozostałych stron i mapa
w treści (#2) są bez zmian. PDF nie jest w repozytorium.

PASS: `python3 tools/check_site.py`, `python3 tools/make_content_template.py --check`
(418 wierszy, puste F/G) i `npm run check:browser` (45 widoków, axe, brak błędów
JS i zasobów). Zrzuty hero przy 2× dla 320, 768 i 1440 px pokazują całe, ostre
koło; przeglądarka wybiera wariant o co najmniej 2 px obrazu na 1 px CSS.
Zaokrąglony róg nie ucina koła przy szerokości okna od 300 do 1600 px.

Demo Katarzyny Chałas przebudowano: strona główna i osiem podstron, nowa paleta,
lokalne Allrounder/Montserrat, nowe zdjęcia oraz pełne teksty z Excela i briefu.
Praca jest w gałęzi `feat/issue-1-brand-rebuild`; źródłowy `main` to `e92207f`.

## Wdrożony zakres

- Pełne O zmianie nad O mnie; O mnie z T023/T024 i linkiem do Mojej drogi.
- Moja/Twoja droga oraz sześć kart w ustalonej kolejności prowadzą do ośmiu
  zwykłych plików HTML. Sekcję Narzędzia i odnośniki usunięto.
- Podstrony mają wspólny banner z nową fotografią, pełne opisy, listy,
  wyróżnienia, zachowane placeholdery i CTA do `index.html#kontakt`.
- Cennik jest listą definicji na stronie głównej i Warsztatach; coaching
  400–600 zł, interwencja 250 zł, MTQ Plus „do uzupełnienia”. Zachowano też
  zdanie o trudnościach finansowych i wszystkie dotychczasowe cele CTA.
- RAPID poprawiono wyłącznie w pięciu angielskich nazwach; ujednolicono MTQ Plus,
  zachowano oboczność terapia/masaż, przypisanie cytatu i treść biografii.
- Mapa PRISM jest konkretnym obrazem z briefu z podpisem źródła. Zachowano
  odnośniki do praktyków PRISM, listy IPTK oraz numer certyfikatu.
- Wzorzec Excel obejmuje 9 stron i 418 unikalnych ID; eksport chroni wypełnione
  arkusze i ma zaktualizowany `--check`. Nie dodano importera ani CMS-a.
- Każda strona ma własne meta, jeden H1, skip-link, dostępne menu mobilne
  i `noindex,nofollow`. Lokalny serwer nie udostępnia dokumentów źródłowych.

## Weryfikacja i odtworzenie

```bash
python3 tools/serve_demo.py           # http://127.0.0.1:8765
python3 tools/make_content_template.py
npm run check
npm ci
npm run check:browser
# Z interpreterem zawierającym zależności tools/requirements-source-audit.txt:
python tools/check_source_materials.py
```

PASS: 9 stron, 201 lokalnych odnośników/zasobów, 418 wierszy eksportu,
109 starych ID, 45 wpisów F / 16 usunięć, 16 instrukcji G, 131 bloków PDF
i hashe wszystkich pięciu oryginałów. Browser QA: 45 widoków od 320 px,
8 kompletnych ścieżek do kontaktu, klawiatura, menu, reduced-motion i brak JS.
Brak błędów JS/zasobów i zgłoszonych naruszeń axe. Obraz kontaktowy ma 60%
obu dawnych wymiarów w pięciu porównanych widokach.

Szczegóły, ograniczenia testów i źródła: [docs/QA.md](docs/QA.md).
Mapowanie treści: [docs/source-mapping.md](docs/source-mapping.md).
Lokalne zrzuty i JSON: `artifacts/browser/` (ignorowane w Git).

## Zależność od właściciela

Font nagłówków nie jest już zależnością. W karcie **1879** właścicielka wybrała
Cormorant Infant (SIL OFL 1.1) zamiast Allrounder Antiqua Test bez polskich glifów.
[Źródło, podzbiór i dopasowanie wagi](assets/fonts/README.md).

LinkedIn zwraca automatycznemu klientowi HTTP 999. Zachowany dokładny URL,
otwarcie nowej karty i bezpieczny brak `window.opener` są sprawdzone.
Nie testowano fizycznych telefonów, Safari, Firefoksa ani czytnika ekranu.

## Publikacja

Przebudowa jest już na GitHub Pages pod
<https://ponurson.github.io/Katarzyna_chalas_page/>. Wykonano to osobnym zadaniem:
`feat/issue-1-brand-rebuild` scalono do `main` (fast-forward), a Pages buduje
z `main` / `/`. Konfiguracji Pages, widoczności repo ani `noindex,nofollow`
nie zmieniono. Font rozstrzygnięto później w karcie 1879.

Przed zakończeniem porównywane są lokalny HEAD i ref tej gałęzi na origin.
Commit można odczytać przez `git log -1 --oneline`; bieżący stan przez
`git status --short --branch`. Żaden z pięciu surowych plików wejściowych nie
wchodzi do commita. Usunięto ze śledzenia wygenerowany wcześniej `__pycache__`.
