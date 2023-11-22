# 3. buatlah fungsi untuk mencetak nilai bilangan ganjil dari parameter yang di masukan :
# ex : ganjil (100)

print("______________________________________________")

def ganjil(batas):
    for i in range(batas + 1):
        if i % 2 != 0:
            print("Angka ganjil ditemukan: ", i)

ganjil(100)

print("______________________________________________")