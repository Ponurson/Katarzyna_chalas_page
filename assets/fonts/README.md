# Fonty demo

Fonty są lokalne: strona nie pobiera ich z Google Fonts ani prywatnego dysku.

| Pliki | Użycie | Źródło i warunki |
| --- | --- | --- |
| `AllrounderAntiquaTest-Regular.woff` | Nagłówki, marka, wyróżnione hasła; prawdziwa odmiana Regular, 400 | [Pakiet wskazany przez właściciela](https://font.download/font/allrounder-antiqua-test), [zapis warunków](Allrounder-NOTICE.txt) |
| `AllrounderAntiquaTest-RegularItalic.woff` | Cytat; prawdziwa kursywa, bez sztucznego pochylenia | Ten sam pakiet i warunki |
| `Montserrat-Variable.woff2` | Akapity, listy, nawigacja, CTA; wagi 100–900 | [Google Fonts: Montserrat](https://github.com/google/fonts/tree/main/ofl/montserrat), [dołączona SIL OFL 1.1](Montserrat-OFL.txt) |

Allrounder: oba pliki WOFF są identyczne bajtowo z pobranym pakietem web
(ponownie porównane 2026-09-06). Nie modyfikowano fontów ani ich copyrightu.
Montserrat jest lokalnym wariantem WOFF2 obejmującym łaciński zestaw znaków,
w tym wszystkie polskie litery, z fontu zmiennego `Montserrat[wght].ttf`.

## Ograniczenie wskazanego pakietu Test

Każda użyta odmiana Allrounder Test ma w mapie Unicode 71 znaków i **nie ma**
`ĄĆĘŁŃÓŚŹŻąćęłńóśźż`. Te litery pozostają prawidłowym tekstem Unicode;
przeglądarka rysuje je fontem zapasowym `Georgia, serif`. Ich kształt może się
różnić od pozostałych liter. Allrounder nadal faktycznie rysuje dostępne glify
nagłówków i cytatu. Montserrat zawiera komplet polskich znaków.

Pełna zgodność kroju polskich liter wymaga pełnego fontu i odpowiednich
uprawnień od właściciela. Sprawę zapisano w Super Jirce, projekt 1753,
kolumna `next_steps`, karta **1879**; istnienie karty potwierdzono 2026-09-06.
Nie kupiono licencji i nie zadeklarowano uprawnień produkcyjnych.

Lista plików i warunków pakietu znajduje się w `Allrounder-NOTICE.txt`.
Kontrola przeglądarkowa zapisuje faktyczne załadowanie odmian w raporcie QA.
