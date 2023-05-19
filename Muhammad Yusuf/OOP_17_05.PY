class Avto:
    def __init__(self):
        self.model =input("Mashinangiz modelini kiriting: ")
        self.rangi = input("Mashinangiz rangini kiriting: ")
        self.karobka = input("Mashinangiz karobkasini kiriting: ")
        self.narhi = input("Mashinangiz narhini kiriting: ")
        self.yili = input("Mashinangiz yilini kiriting: ")
    def get_info(self):
        return f"Mashinaning modeli: {self.model}\n rangi {self.rangi}\n karo'bkasi {self.karobka}\n sotilgan narhi {self.narhi}\n chiqqan yili: {self.yili}"
    
    
mashina = Avto()
print(mashina.get_info())



class Tezlik:
    def set_bosqich (self,km):
        self.km = km
        