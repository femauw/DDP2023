# Membuat Modul perhitungan luas dan keliling bangun datar

def persegi(sisi):
    luas = sisi * sisi
    keliling = sisi * 4
    print("Luas Persegi: ", luas)
    print("Keliling Persegi: ", keliling)

def persegi_panjang(p, l):
    luas = p * l
    keliling = 2 * (p + l)
    print("Luas Persegi panjang: ", luas)
    print("Keliling Persegi panjang: ", keliling)

def lingkaran(r):
    phi = 3.14
    luas = phi * r * r
    keliling = 2 * phi * r
    print("Luas Lingkaran: ", luas)
    print("Keliling Lingkaran: ", keliling)

def segitiga(a, t):
    luas = 1/2 * a * t
    keliling = a * 3
    print("Luas Segitiga sama sisi: ", luas)
    print("Keliling Segitiga sama sisi: ", keliling)

def belah_ketupat(d1, d2, s):
    luas = 1/2 * d1 * d2
    keliling = 4 * s
    print("Luas Belah Ketupat: ", luas)
    print("Keliling Belah Ketupat: ", keliling)

def jajar_genjang(a, t, sm):
    luas = a * t
    keliling = 2 * (a + sm)
    print("Luas Jajar Genjang: ", luas)
    print("Keliling Jajar Genjang: ", keliling)

def layang_layang(d1, d2, sisi_atas, sisi_bawah):
    luas = 1/2 * d1 * d2
    keliling = 2 * (sisi_atas + sisi_bawah)
    print("Luas Layang-layang: ", luas)
    print("Keliling Layang-layang: ", keliling)