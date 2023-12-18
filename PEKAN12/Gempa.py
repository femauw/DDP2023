class Gempa:
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    def dampak(self):
        if self.skala < 2:
            print ("Gempa pada daerah",self.lokasi,"dengan skala",self.skala,"Gempa ini tidak berasa")
        elif 2 <= self.skala < 4:
            print("Gempa pada daerah",self.lokasi,"dengan skala",self.skala, "Dampak dari gempa ini bangunan retak-retak")
        elif 4 <= self.skala < 6:
            print("Gempa pada daerah",self.lokasi,"dengan skala",self.skala, "Dampak dari gempa ini dapat membuat bangunan roboh")
        else:
            print("Gempa pada daerah",self.lokasi,"dengan skala",self.skala, "Dampak dari gempa ini dapat membuat bangunan roboh dan berpotensi terjadinya tsunami")