# 2. buatlah fungsi untuk mencari kelulusan nilai dari berikut : 
# jika nilai < 60 maka gagal 
# jika nilai = 61 - 70 maka baik 
# jika nilai = 71 - 80 maka sangat baik 
# jika nilai = 81 - 100 maka istimewa 
# ex:
# nilai (60)

print("______________________________________________")

nilai = int(input("Masukkan nilai: "))

def nilai_kelulusan(nilai):
    if nilai < 0:
        return "NILAI YANG ANDA MASUKKAN TIDAK VALID!!!"
    elif nilai < 60:
        return "GAGAL"
    elif nilai <= 70:
        return "BAIK"
    elif nilai <= 80:
        return "SANGAT BAIK"
    elif nilai <= 100:
        return "ANAK DEWA"
    else:
        return "NILAI YANG ANDA MASUKKAN TIDAK VALID!!!"

print(nilai_kelulusan(nilai))

print("______________________________________________")