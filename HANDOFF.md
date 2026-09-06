# Handoff — issue #1

Aktualizacja po review: monogram KC, ciemny nagłówek, wyrównane kolumny tekstu
i zdjęć, przywrócone tła i kafelki, Montserrat Bold w Dla biznesu, baner oraz
cennik. Szczegóły i pomiary laptopów/telefonów:
[raport zmian po review](docs/review-2026-09-06.md).
Poniżej zapis pierwotnego wdrożenia i późniejszej konfiguracji publikacji.

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
- Wzorzec Excel obejmuje 9 stron i 682 unikalne ID; eksport chroni wypełnione
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

PASS: 9 stron, 201 lokalnych odnośników/zasobów, 682 wiersze eksportu,
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
