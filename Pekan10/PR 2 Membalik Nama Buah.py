buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
fruit = []

for i in range(len(buah)):
    balikan = len(buah) - i - 1
    fruit.insert(i, buah[balikan])

print(fruit)