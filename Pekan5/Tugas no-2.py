# Tugas 2
# Buat Program python dengan match case untuk menghitung luas bangun datar:
# jika pilih 1, maka menghitung luas persegi
# jika pilih 2, maka menghitung luas lingkaran
# jika pilih 3, maka menghitung luas segitiga
# selain pilihan diatas, maka keterangan : salah pilihan

print("""menghitung luas bangun datar

    pilih bangun datar yang akan dihitung
    1. Menghitung luas persegi
    2. Menghitung luas lingkaran
    3. Menghitung luas segitiga
    """)

bangun_datar=int(input("masukkan angka"))

match bangun_datar:
    case 1:
        s = int(input("masukkan angka"))
        rumus1 = (s * s)
        print("Hasil dari perhitungan luas persegi adalah", rumus1)
    case 2:
        r = int(input("masukkan angka"))
        π = int(3.14)
        rumus2 = (π * r * r)
        print("Hasil dari perhitungan luas lingkaran adalah", rumus2)
    case 3:
        a = int(input("masukkan angka"))
        t = int(input("masukkan angka"))
        rumus3 = (1/2 * a * t)
        print("hasil dari perhitungan luas segitiga adalah", rumus3)
    case _:
        print("pilihan yang anda masukkan tidak valid")