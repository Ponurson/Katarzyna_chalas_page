# Fonty demo

Fonty są lokalne: strona nie pobiera ich z Google Fonts ani prywatnego dysku.

| Pliki | Użycie | Źródło i warunki |
| --- | --- | --- |
| `CormorantInfant-Variable.woff2` | Nagłówki, marka, wyróżnione hasła; waga 530 | [Google Fonts: Cormorant Infant](https://github.com/google/fonts/tree/main/ofl/cormorantinfant), [dołączona SIL OFL 1.1](CormorantInfant-OFL.txt) |
| `CormorantInfant-Italic-Variable.woff2` | Cytat; prawdziwa kursywa, waga 560 | Ten sam projekt i licencja |
| `Montserrat-Variable.woff2` | Akapity, listy, nawigacja, CTA; wagi 100–900 | [Google Fonts: Montserrat](https://github.com/google/fonts/tree/main/ofl/montserrat), [dołączona SIL OFL 1.1](Montserrat-OFL.txt) |

Cormorant Infant (Christian Thalmann, Copyright 2015 The Cormorant Project
Authors) zastąpił Allrounder Antiqua Test decyzją właścicielki z karty **1879**.
OFL pozwala używać fontu na stronie i dołączać go do witryny bez opłat.
Pliki Allroundera usunięto z repozytorium.

Oba WOFF2 to podzbiory fontów zmiennych `CormorantInfant[wght].ttf`
(SHA-256 `48c6efe07539c75d3108795467898706a9cd71ce876d461e45f58482156d7bf3`)
i `CormorantInfant-Italic[wght].ttf`
(`d5f81edef82cf31c093d057709e1bfb42aa776aacf78651b14f9817c2decb251`)
z google/fonts @ `3dd7884`, wersja 4.001. Zachowują oś `wght` 300–700,
kerning i polskie formy `locl`. Nie zmieniano obrysów ani nazw:

```bash
pyftsubset 'CormorantInfant[wght].ttf' --unicodes='U+0000-024F,U+2000-206F,U+20A0-20C0,U+2122' \
  --flavor=woff2 --output-file=CormorantInfant-Variable.woff2   # fonttools 4.65.0 + brotli
```

Zakres obejmuje łacinę z rozszerzeniami A i B, w tym `ĄĆĘŁŃÓŚŹŻąćęłńóśźż`,
interpunkcję, waluty i ™. Kontrola przeglądarkowa odczytuje z DevTools fonty,
które faktycznie narysowały nagłówki, markę, hasła i cytat. Font systemowy
w tym miejscu oznacza brakujący glif i przerywa test.

## Dopasowanie wagi do Allroundera

Wagi ustawiają `--serif-weight` i `--serif-italic-weight` w `styles.css`.
Porównano Allrounder Antiqua Test Regular/Italic z Cormorant Infant w wagach
300–700. Próbą były wszystkie znaki tekstów szeryfowych dziewięciu stron
(nagłówki, marka, hasła, cytat) obecne w obu fontach, liczone z częstością
występowania. Odmiany Test nie mają polskich liter, więc te znaki pominięto.

Cormorant ma dużo mniejszą wysokość x: 386 wobec 494 jednostek na 1000
(78 %), wersaliki 625 wobec 720. Waga jest więc porównana względem wysokości
liter, tak jak odmiany jednej rodziny. Główna miara to średnia grubość kreski,
czyli 2 × pole / obwód konturu glifu, podzielona przez wysokość x. Obejmuje
trzony, łuki i cienkie kreski. Pozostałe miary pokazują rozrzut:

| Miara | Allrounder Regular | Równa waga Cormorant | Allrounder Italic | Równa waga Cormorant Italic |
| --- | --- | --- | --- | --- |
| **Średnia grubość kreski / wysokość x** | 0,1266 | **529** | 0,1180 | **564** |
| Pokrycie: pole liter / (szerokość × wysokość x) | 0,3598 | 506 | 0,3667 | 514 |
| Trzon „l” w połowie wysokości x / wysokość x | 0,1721 | 467 | 0,1693 | 529 |
| Trzon „H” / wysokość wersalików | 0,1306 | 516 | 0,1306 | 583 |

Wybrano 530 dla pisma prostego i 560 dla kursywy. Regular 400 jest wyraźnie
lżejszy od Allroundera: średnia grubość kreski względem wysokości x to 82 %.
Przy tych samych rozmiarach CSS litery Cormoranta są mniejsze, więc kreska
jest cieńsza w pikselach: 78 % Allroundera. Nie da się tego wyrównać samą
wagą, bo nawet Bold 700 daje 97 %. Rozmiarów nie zmieniano.
