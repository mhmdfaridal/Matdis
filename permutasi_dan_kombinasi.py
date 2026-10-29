import math
import itertools
from utils import jeda, garis

def permutasiDanKombinasi(mahasiswa, r):
    # Data Mahasiswa
    n = len(mahasiswa)

    print(f"Terdapat {n} mahasiswa: {', '.join(mahasiswa)}.\n")

    # ==========================================
    # STUDI KASUS 1: PERMUTASI (Urutan Penting)
    # ==========================================
    print("--- STUDI KASUS 1: PERMUTASI ---")
    print(f"Kasus: Akan dipilih {r} orang untuk menempati jabatan berbeda (urutan penting).")
    print("Berapa banyak susunan kepengurusan yang mungkin dibuat?\n")

    jeda()

    total_permutasi = math.perm(n, r)
    # Pembilang: deret n turun sebanyak r angka (contoh: 4 x 3)
    proses_p = " x ".join(str(i) for i in range(n, n - r, -1))

    # Menampilkan hasil perhitungan
    print(f"\nPermutasi P({n}, {r}) = {n}! / ({n}-{r})! adalah {total_permutasi}")
    print(f"Hasil dari: {proses_p}")
    # Label jabatan mengikuti jumlah r (contoh r = 2: Jabatan 1, Jabatan 2)
    jabatan = [f"Jabatan {j}" for j in range(1, r + 1)]
    print(f"Banyaknya Cara ({', '.join(jabatan)}):\n")

    # Menghasilkan dan menampilkan daftar permutasi menggunakan itertools
    susunan_p = list(itertools.permutations(mahasiswa, r))

    for i, susunan in enumerate(susunan_p, start=1):
        # Setiap unsur berurutan menempati jabatan sesuai posisinya
        format_susunan = ", ".join(f"{orang} ({label})" for orang, label in zip(susunan, jabatan))
        print(f"{i}. {format_susunan}")

    jeda()

    # ==========================================
    # STUDI KASUS 2: KOMBINASI (Urutan Tidak Penting)
    # ==========================================
    garis()
    print("\n--- STUDI KASUS 2: KOMBINASI ---")
    print(f"Kasus: Akan dipilih {r} orang untuk menjadi perwakilan tim proyek tanpa jabatan.")
    print("Berapa banyak susunan tim yang mungkin dibuat?\n")

    jeda()

    total_kombinasi = math.comb(n, r)
    pembilang_c = " x ".join(str(i) for i in range(n, n - r, -1))
    penyebut_c = " x ".join(str(i) for i in range(r, 0, -1))
    proses_c = f"({pembilang_c}) / ({penyebut_c})"

    # Menampilkan hasil perhitungan
    print(f"\nKombinasi C({n}, {r}) = {n}! / ({r}!({n}-{r})!) adalah {total_kombinasi}")
    print(f"Hasil dari: {proses_c}")
    print("Banyaknya Cara (Anggota Tim):\n")

    # Menghasilkan dan menampilkan daftar kombinasi menggunakan itertools
    susunan_c = list(itertools.combinations(mahasiswa, r))

    for i, susunan in enumerate(susunan_c, start=1):
        format_susunan = ", ".join(susunan)
        print(f"{i}. {format_susunan}")

    # Kesimpulan gabungan
    print(f"\nKarena jabatan berbeda (urutan penting), jumlahnya")
    print(f"P({n}, {r}) = {total_permutasi}. Susunan tim biasa dihitung dengan")
    print(f"C({n}, {r}) = {total_kombinasi}, yaitu P({n}, {r}) / {r}!.")

if __name__ == "__main__":
    pass