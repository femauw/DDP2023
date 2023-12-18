from Gempa import *

gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

Banten = gempa1.dampak()
Palu = gempa2.dampak()
Cianjur = gempa3.dampak()
Jayapura = gempa4.dampak()
Garut = gempa5.dampak()
