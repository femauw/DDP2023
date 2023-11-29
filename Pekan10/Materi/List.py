# Berisi sekumpulan data dengan urutan tertentu, bisa ada duplikasi
# Array bisa merupakan implementasi dari list
# Null = Kosong 

buah = ["duren", 'jambu', 'rambutan', 'mangga', 'ppya']

# menghitung panjang list
print(len(buah))

# cek keberadaan nilai
if 'durian' in buah:
    print('buah ada')
else:
    print('buah tidak kompatibel di perangkat anda')

# Looping
for fruit in buah:
    print(fruit)