import math
import itertools

def kombinasiBatasan(laki_laki, perempuan, r):
    semua_mahasiswa = laki_laki + perempuan
    
    print("\n--- CARA 1: PERHITUNGAN MATEMATIS (KOMPLEMEN) ---")
    # Menghitung semua kemungkinan tanpa batasan
    total_semua_tim = math.comb(len(semua_mahasiswa), r)
    
    # Menghitung tim yang melanggar syarat (HANYA laki-laki)
    tim_hanya_laki_laki = math.comb(len(laki_laki), r)
    
    # Menghitung tim yang valid
    tim_valid_math = total_semua_tim - tim_hanya_laki_laki
    
    print(f"Semua tim C({len(semua_mahasiswa)}, {r})     = {total_semua_tim}")
    print(f"Tim tanpa perempuan C({len(laki_laki)}, {r}) = {tim_hanya_laki_laki}")
    print(f"Jawaban: {total_semua_tim} - {tim_hanya_laki_laki} = {tim_valid_math} tim\n")

    print("--- CARA 2: FILTERING PROGRAM ---")
    semua_kombinasi = list(itertools.combinations(semua_mahasiswa, r))
    tim_valid_program = []
    
    # Memfilter menggunakan logika keberadaan anggota dari list 'perempuan'
    for susunan in semua_kombinasi:
        ada_perempuan = any(anggota in perempuan for anggota in susunan)
        if ada_perempuan:
            tim_valid_program.append(susunan)

    print(f"Jumlah tim yang berhasil difilter program: {len(tim_valid_program)} tim")
    
    if tim_valid_math == len(tim_valid_program):
        print("Status: TERBUKTI SAMA antara hitungan rumus dan filter program!\n")

    print("Contoh 5 susunan pertama yang valid:")
    # Menampilkan maksimal 5 saja agar rapi
    for i, susunan in enumerate(tim_valid_program, start=1):
        format_susunan = ", ".join(susunan)
        print(f"{i}. {format_susunan}")

if __name__ == "__main__":
    pass