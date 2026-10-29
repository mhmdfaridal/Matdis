import math
import itertools

def permutasiPerulangan(elemen, r):

    n = len(elemen)
    total = math.pow(n, r)
    proses = " x ".join(str(n) for i in range(r))

    susunan = list(itertools.product(elemen, repeat=r))

    print(f"\nPermutasi P = n^r adalah {int(total)}")
    print(f"Hasil dari: {proses}")

    print("Banyaknya Cara:\n")

    nomor = 1
    for i in susunan:
        print(f"{nomor}. [{', '.join(i)}]")
        nomor += 1