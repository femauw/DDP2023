# Untuk menyimpan data yang diakses bukan dengan indeks
# Data disimpan sebagai pasangan dari key dan value
# Dituliskan dengan diapit kurung kurawal { } dan dipisah dengan titik dua 

data_diri = {"nama":"Faqih", "matkul":"DDP"}

# Mengases Dictionary
print(data_diri["nama"])

# Menambah item
data_diri["jurusan"] = "Teknik Informatika"
print(data_diri)

# update item
data_diri["nama"] = "Murobbie"
print(data_diri)

# Mengahapus item
data_diri.pop("matkul")
print(data_diri)

# Cek keberadaan key
if("nama" in data_diri):
    print("Terdapat Nama")
else:
    print("Nama Tidak Terdapat")