class orang:
    def __init__(self, fnama, lnama):
        self.fnama = fnama
        self.lnama = lnama

    def makan(self):
        print("saya bisa makan")

    def cetak(self):
        print("nama saya",self.fnama, self.lnama)

class mahasiswa(orang):
    def __init__(self, fnama, lnama, prodi, angkatan):
        super().__init__(fnama, lnama)
        self.prodi = prodi
        self.angkatan = angkatan

    def cetak(self):
        print("nama saya", self.fnama, self.lnama,"Prodi saya",self.prodi, "angkatan ", self.angkatan)

class pegawai(orang):
    def bekerja(self):
        print("saya bekerja", self.fnama, self.lnama)


x = orang("agus", "dwikunto")
x.cetak()

y = mahasiswa("aqih", "eaaa", "TI", 2023)
y.cetak()
y.makan()

z = pegawai("upiw", "yahya")
z.bekerja()