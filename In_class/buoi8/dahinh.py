class Toyota:
    def dungxe(self):
        print("Toyota dung xe de nap dien")
    def nomay(self):
        print("Toyota no may bang hop so tu dong")

class Porshe:
    def dungxe(self):
        print("Toyota dung xe de bom xang")
    def nomay(self):
        print("Toyota no may bang hop so co") 

def kiemtra_dungxe(car): car.dungxe()

toyota = Toyota()
porshe = Porshe()

kiemtra_dungxe(toyota)
kiemtra_dungxe(porshe)
