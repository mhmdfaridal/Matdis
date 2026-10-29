from utils import menu, jeda, garis, bersihkanLayar
from permutasi_n import permutasiN
from permutasi_r_dari_n import permutasiRN
from kombinasi import kombinasi
from kombinasi_perulangan import kombinasiPerulangan
from kombinasi_batasan import kombinasiBatasan
from permutasi_perulangan import permutasiPerulangan
from permutasi_unsur_identik import permutasi_unsurIdentik
from permutasi_melingkar import permutasiMelingkar

if __name__ == "__main__":

    isRunning = True

    while(isRunning):

        bersihkanLayar()
        menu()
        pilihan = int(input("> "))

        if pilihan == 0:
            isRunning = False
        if pilihan == 1:
            pass
        elif pilihan == 2:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Ada 4 mahasiswa: M, N, O, dan P yang akan\nmaju presentasi tugas Matematika Diskrit.\nBerapa banyak susunan giliran urutan presentasi yang\nmungkin dibuat dari keempat mahasiswa tersebut?")

            jeda()

            mahasiswa = ["M", "N", "O", "P"]
            permutasiN(mahasiswa)

            jeda()
        elif pilihan == 3:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Sebuah gembok loker membutuhkan kode pengaman yang terdiri\ndari 3 angka berbeda. Angka-angka tersebut hanya boleh dipilih\ndari kumpulan 5 angka yang tersedia, yaitu: 1, 2, 3, 4,\n5.\n\nBerapa banyak kemungkinan kode pengaman yang dapat dibuat?")

            jeda()

            jumlahObjek = ['1', '2', '3', '4', '5']
            jumlahDipilih = 3
            permutasiRN(jumlahObjek, jumlahDipilih)

            jeda()
        elif pilihan == 4:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Berapa string biner panjang 4?\nSetiap posisi memiliki 2 pilihan, yaitu 0 dan 1.")

            jeda()

            jumlahObjek = ['0', '1']
            panjang = 4
            permutasiPerulangan(jumlahObjek, panjang)

            jeda()
        elif pilihan == 5:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print(f"Farid memiliki 1 kata berisi 5 karakter, yaitu \"MALAM\".\nJika Farid ingin mengacak urutan karakter agar menjadi sebuah kata baru,\nada berapa banyak susunan kata yang dapat dibuat?\n(unsur identik M = 2, A = 2, L = 1 )")

            jeda()

            teks = "MALAM"
            permutasi_unsurIdentik(teks)

            jeda()
        elif pilihan == 6:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Lima orang, yaitu A, B, C, D, dan E, duduk mengelilingi meja bundar. Berapa susunan duduk yang berbeda jika susunan yang hanya berbeda karena rotasi dianggap sama?.")

            jeda()

            orang = ["A", "B", "C", "D", "E"]
            # panjang = 5
            permutasiMelingkar(orang)

            jeda()

        elif pilihan == 7:
            bersihkanLayar()
            print("Studi Kasus:\n")
            print("Ada 4 mahasiswa: M, N, O, dan P.")
            print("Akan dipilih 2 orang untuk menjadi perwakilan tim proyek Matematika Diskrit.")
            print("Berapa banyak susunan tim (kombinasi) yang mungkin dibuat dari keempat mahasiswa tersebut?\n")

            jeda()

            mahasiswa = ['M', 'N', 'O', 'P']
            jumlahDipilih = 2
            kombinasi(mahasiswa, jumlahDipilih)

            jeda()

        elif pilihan == 8:
            laki_laki = ['L1', 'L2', 'L3', 'L4', 'L5']
            perempuan = ['P1', 'P2', 'P3', 'P4']
            jumlahDipilih = 3                           
            
            bersihkanLayar()
            print("Studi Kasus:\n")
            print(f"Dari 5 laki-laki dan 4 perempuan, akan dipilih 3 mahasiswa.")
            print("Syarat: Tim harus memiliki MINIMAL SATU perempuan.")
            print("Berapa banyak susunan tim yang mungkin dibuat?\n")
            
            jeda()
            
            # Memanggil fungsi modul
            kombinasiBatasan(laki_laki, perempuan, jumlahDipilih)
            
            jeda()

        elif pilihan == 10:
                    jenis_donat = ['Cokelat', 'Stroberi', 'Matcha']
                    n = len(jenis_donat) # 3 jenis
                    jumlahDipilih = 4                # 4 donat yang akan dipilih
                    
                    bersihkanLayar()
                    print("Studi Kasus:\n")
                    print(f"Terdapat n jenis donat: {', '.join(jenis_donat)}.")
                    print("Akan dibeli 4 buah donat. Setiap jenis rasa persediaannya cukup (boleh dipilih berulang).")
                    print("Berapa banyak kombinasi rasa donat yang bisa dibawa pulang?\n")
        
                    jeda()
        
                    kombinasiPerulangan(jenis_donat, jumlahDipilih)
        
                    jeda()

        else:
            print("Pilihan Tidak Valid")