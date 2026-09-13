# Handoff — issue #1

Aktualizacja po review: monogram KC, ciemny nagłówek, wyrównane kolumny tekstu
i zdjęć, przywrócone tła i kafelki, Montserrat Bold w Dla biznesu, baner oraz
cennik. Szczegóły i pomiary laptopów/telefonów:
[raport zmian po review](docs/review-2026-09-06.md).
Poniżej zapis pierwotnego wdrożenia i późniejszej konfiguracji publikacji.

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

Wskazany Allrounder Antiqua **Test** nie zawiera polskich glifów. Demo używa
prawdziwych Regular/Regular Italic, a brakujące znaki rysuje systemowy serif.
Pełny font z polskimi literami i uprawnieniami wymaga dostarczenia przez właściciela.
Istniejąca karta Super Jirki **1879**, projekt 1753, `next_steps`, została
zweryfikowana; nie utworzono duplikatu. [Źródło i warunki](assets/fonts/README.md).
Nie kupiono licencji ani nie uznano pakietu Test za licencję produkcyjną.

LinkedIn zwraca automatycznemu klientowi HTTP 999. Zachowany dokładny URL,
otwarcie nowej karty i bezpieczny brak `window.opener` są sprawdzone.
Nie testowano fizycznych telefonów, Safari, Firefoksa ani czytnika ekranu.

## Publikacja

Przebudowa jest już na GitHub Pages pod
<https://ponurson.github.io/Katarzyna_chalas_page/>. Wykonano to osobnym zadaniem:
`feat/issue-1-brand-rebuild` scalono do `main` (fast-forward), a Pages buduje
z `main` / `/`. Konfiguracji Pages, widoczności repo ani `noindex,nofollow`
nie zmieniono. Warunki fontu pozostają osobnym zakresem.

Przed zakończeniem porównywane są lokalny HEAD i ref tej gałęzi na origin.
Commit można odczytać przez `git log -1 --oneline`; bieżący stan przez
`git status --short --branch`. Żaden z pięciu surowych plików wejściowych nie
wchodzi do commita. Usunięto ze śledzenia wygenerowany wcześniej `__pycache__`.
