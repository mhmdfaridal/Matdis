from collections import Counter
import math

def permutasi_unsurIdentik(teks):
    teks = teks.upper()
    n = len(teks)
    frekuensi = Counter(teks)
    susunan = []

    pembilang = math.factorial(n)
    penyebut = 1
    for hitung in frekuensi.values():
        penyebut *= math.factorial(hitung)

    def bangun_kata(jalur, sisa_huruf):
        if len(jalur) == len(teks):
            susunan.append(" ".join(jalur))
            return

        for char in sisa_huruf:
            if sisa_huruf[char] > 0:
                sisa_huruf[char] -= 1
                jalur.append(char)

                bangun_kata(jalur, sisa_huruf)

                jalur.pop()
                sisa_huruf[char] += 1

    bangun_kata([], frekuensi)
    print(f"\nTeks: {teks}")
    print(f"Banyaknya kata: {pembilang // penyebut}")
    print(f"Seluruh susunan: ")
    nomor = 1
    for kata in susunan:
        print(f"{nomor}. {kata}")
        nomor += 1