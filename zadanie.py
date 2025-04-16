palety = [
    (17, 350),
    (12, 200),
    (25, 123),
    (32, 87)
]

ladunki = []
for ilosc, waga in palety:
    ladunki.extend([waga] * ilosc)

pojazdy = {
    "zielony": 1000,
    "niebieski": 1500,
    "czerwony": 2000
}

ladunki.sort(reverse=True)

def pakuj_ladunki_na_pojazdy(ladunki, pojemnosci):
    pojazdy_uzyte = []

    for ladunek in ladunki:
        zaladowano = False
        for pojazd in pojazdy_uzyte:
            if pojazd[0] + ladunek <= pojazd[1]:
                pojazd[0] += ladunek
                zaladowano = True
                break
        if not zaladowano:
            for typ, pojemnosc in sorted(pojemnosci.items(), key=lambda x: x[1]):
                if ladunek <= pojemnosc:
                    pojazdy_uzyte.append([ladunek, pojemnosc, typ])
                    break
    return pojazdy_uzyte

pojazdy_uzyte = pakuj_ladunki_na_pojazdy(ladunki, pojazdy)

from collections import Counter
licznik = Counter([p[2] for p in pojazdy_uzyte])

print("Potrzebne pojazdy:")
for kolor in ["zielony", "niebieski", "czerwony"]:
    print(f"{kolor}: {licznik.get(kolor, 0)} szt.")

print(f"\nŁączna liczba samochodów: {sum(licznik.values())}")
