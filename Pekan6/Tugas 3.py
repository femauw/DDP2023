# Buat program untuk minta input jumlah baris dan buat
# rangkaian berikut ini
# *
# **
# ***
# ****
# Dan seterusnya sejumlah baris yang diinputkan
# Gunakan for loop dengan range
baris = int(input ('masukkan baris:'))
for i in range (1,baris + 1):
    print(i * "*")