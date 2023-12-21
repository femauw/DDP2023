# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)
# buat minimal 3 class child (badak, ikan, ular, dll) setiap class child itu memiliki 2 properti dan method

class Animal:
    def __init__(self, name, makanan, habitat, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.habitat = habitat
        self.berkembang_biak = berkembang_biak

class Badak(Animal):
    def __init__(self, name, makanan, berat):
        super().__init__(name, makanan, "habitat", "berkembang_biak")
        self.berat = berat

    def cetak(self):
        print("Nama Badak\t:", self.name,"\tMakanannya\t:", self.makanan)
        print(self.name, "Memiliki berat", self.berat, "ton")

class Ikan(Animal):
    def __init__(self, name, habitat, warna):
        super().__init__(name, "makanan", habitat, "berkembang_biak")
        self.warna = warna

    def cetak(self):
        print("Nama Ikan\t:", self.name,"\tHabitat\t\t:", self.habitat)
        print(self.name, "Memiliki warna", self.warna)

class Ular(Animal):
    def __init__(self, name, berkembang_biak, ganti_kulit):
        super().__init__(name, "makanan", "habitat", berkembang_biak)
        self.ganti_kulit = ganti_kulit

    def cetak(self):
        print("Nama Ular\t:", self.name, "\tBerkembang biak\t:", self.berkembang_biak)
        print(self.name, self.ganti_kulit)


x = Badak("Badak Jawa", "Rumput", "3")
x.cetak()

y = Ikan("Ikan Badut", "Terrumbu Karang", "oranye putih")
y.cetak()

z = Ular("Ular Derik", "bertelur", "berganti kulit")
z.cetak()