buah = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
duplikat = 2

dupe = [item for item in buah for i in range(duplikat)]

print(dupe)