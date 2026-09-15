# Przeniesienie źródeł i Vercel

## Zakres

Docelowy właściciel GitHub: `katarzynachalas`.
Transfer istniejącego repozytorium `Ponurson/Katarzyna_chalas_page` zachowa
historię i issues. Docelowa nazwa: `katarzynachalas/Katarzyna_chalas_page`.
Nie należy tworzyć drugiego repozytorium o tej nazwie przed przyjęciem transferu.

## Stan na koniec pracy — 2026-09-15

Konfiguracja i sprawdzony eksport są w commicie `abdb7db`, wypchniętym na
`origin/main`. Następnie GitHub API przyjęło żądanie transferu repozytorium
(ID `1341669712`) do `katarzynachalas`.
Kontrola po żądaniu nadal wskazuje właściciela `Ponurson`; docelowy adres
repozytorium zwraca HTTP 404. Transfer oczekuje na przyjęcie przez odbiorczynię.
Lokalny `origin` i repo projektu Super Jirka pozostają przy dotychczasowym
adresie do potwierdzenia zakończenia transferu.

Utworzono karty `next_steps` w projekcie 1753:

- **1936** — przyjęcie transferu w ciągu 24 godzin, następnie aktualizacja
  remote oraz repo projektu.
- **1937** — dostęp do Vercel, autoryzacja repozytorium, właściwa domena/DNS
  oraz kontrola rzeczywistej publikacji.

Pełne przepięcie GitHub → Vercel → domena nie jest jeszcze zakończone.

## Gotowa konfiguracja

| Ustawienie | Wartość |
| --- | --- |
| Framework Preset | Other (`framework: null`) |
| Production Branch | `main` |
| Root Directory | katalog główny repozytorium |
| Install Command | pusty, pominięcie instalacji |
| Build Command | `npm run build` |
| Output Directory | `dist` |
| Adresy podstron | zachowane `.html`, bez końcowego `/` |

`tools/build_site.mjs` używa wyłącznie standardowej biblioteki Node.js.
Przed eksportem usuwa poprzedni `dist`, następnie kopiuje jawnie wskazane strony,
CSS, JS oraz obrazy/fonty i licencje OFL z `assets`.
Pliki wejściowe, Excel, dokumentacja i narzędzia nie są częścią publikacji.
Przekształcenie adresów 404 zachodzi tylko w eksporcie; źródłowe 404 pozostaje
zgodne z dotychczasowym podkatalogiem GitHub Pages.

Podstawa ustawień: [dokumentacja Vercel](https://vercel.com/docs/project-configuration/vercel-json).

## Dokończenie po stronie kont

1. Przyjąć transfer na koncie `katarzynachalas`. Zaproszenie GitHub wygasa po
   jednym dniu; po wygaśnięciu trzeba ponowić transfer. Zasady:
   [GitHub — transfer repozytorium](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository).
2. Po potwierdzeniu nowego właściciela przez API zmienić lokalny remote:

   ```bash
   git remote set-url origin https://github.com/katarzynachalas/Katarzyna_chalas_page.git
   git fetch origin
   ```

   Zaktualizować również repo projektu 1753 w Super Jirce. Dotychczasowy URL
   repozytorium GitHub przekierowuje po transferze, ale stary adres GitHub Pages
   nie otrzymuje takiego przekierowania.
3. Na właściwym koncie/teamie Vercel udzielić aplikacji GitHub Vercel dostępu do
   przeniesionego repozytorium. W istniejącym projekcie podłączyć nowe repo w
   Settings → Git; jeśli projekt jeszcze nie istnieje, zaimportować repo.
   Ustawić `main` jako Production Branch i uruchomić deployment.
4. W Settings → Domains ustawić właściwą domenę oraz wariant `www`, według
   danych właścicielki. U rejestratora zastosować rekordy DNS wskazane przez
   ten konkretny projekt Vercel. Potwierdzić poprawną konfigurację i certyfikat
   HTTPS w panelu; nie zgadywać domeny ani wartości rekordów.
5. Sprawdzić opublikowaną stronę główną i osiem podstron na telefonie i desktopie,
   ładowanie zdjęć/fontów, menu, CTA do kontaktu, kotwice oraz stronę 404 pod
   adresem `/nie-ma/takiej-strony`. Błędny adres musi zwracać HTTP 404,
   z działającym CSS i powrotem na stronę główną. Sprawdzić również, że
   `/teksty-strony.xlsx`, `/tools/build_site.mjs` i `/.git/config` zwracają 404.
6. Domknąć istniejącą kartę 1881 dotyczącą indeksowania. Aktualna konfiguracja
   zachowuje `noindex,nofollow`; samo podłączenie domeny nie włącza indeksowania.

## Weryfikacja lokalna

```bash
npm run build
npm run check
SITE_DIR=dist QA_OUTPUT_DIR=artifacts/vercel-browser npm run check:browser
```

Kontrola przeglądarkowa korzysta z eksportu i lokalnego serwera, nie z Vercel.
Nie potwierdza DNS, HTTPS ani ustawień projektu zdalnego.
Artefakty lokalne są w ignorowanym katalogu `artifacts/vercel-browser/`.

### Wyniki — 2026-09-15

- `npm run build` i `npm run check`: PASS; 9 stron, 200 lokalnych
  odnośników/zasobów, 368 wierszy wzorca treści.
- Chromium na `dist`: PASS, 45 widoków (320, 375, 390, 768 i 1440 px),
  osiem pełnych ścieżek nawigacji, menu i CTA; zero błędów JS/sieci i zero
  naruszeń axe. Obejrzano zrzuty hero strony głównej przy 390 i 1440 px.
- Dodatkowa kontrola `/nie-ma/takiej-strony` przy 390 i 1440 px: HTTP 404,
  działający CSS i powrót na stronę główną; brak poziomego przewijania.
- Prywatne pliki i narzędzia: HTTP 404 w lokalnym podglądzie eksportu.
- Eksport zawiera 10 plików HTML; odnośniki `href`/`src` prowadzą do obecnych
  plików. W 404 eksportu nie ma prefiksu GitHub Pages.
- `vercel.json`: walidacja instancji Draft 7 według pobranego schematu Vercel
  zakończona powodzeniem. Pełna walidacja samego schematu przez systemowy
  `jsonschema` nie przeszła dla nieużywanej definicji usług w schemacie dostawcy.
- Dotychczasowe GitHub Pages, przed transferem: dziewięć stron HTTP 200,
  zawartość HTML identyczna bajtowo z checkoutem.

Brak uwierzytelnionej sesji/tokena Vercel w środowisku i brak potwierdzonej
nazwy domeny. Deployment Vercel, DNS i HTTPS domeny docelowej pozostają
niezweryfikowane. Dane logowania nie są częścią repozytorium ani raportów.
