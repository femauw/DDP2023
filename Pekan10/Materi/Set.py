# Set=himpunan, tidak ada dupe, dituliskan dengan {}, acak-acakan

motor = {"beat", "astrea", "pario"}
mobil = {"avanza", "xenia", "Suprax"}

print(motor)

# menambahkan
motor.add("xsr")
print(motor)

# menghapus item
motor.remove("astrea")
print(motor)

# Menggabungkan
kendaraan = motor.union(mobil)
print(kendaraan)

# update set (menggabungkan dengan update)
motor.update(mobil)
print(motor)