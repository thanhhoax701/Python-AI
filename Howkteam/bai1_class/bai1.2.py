class Car:
    def __init__(self, ten, hinhdang, mausac,theloai):
        self.ten = ten
        self.hinhdang = hinhdang
        self.mausac = mausac
        self.theloai = theloai
    def chay(self):
        return self.ten + " co hinh gi?\n" + self.hinhdang + "\nNo co mau: " + self.mausac + ", thuoc loai xe " + self.theloai
car1 = Car("Huracan", "Ai ma biet!!!", "xanh", "dien")
print(car1.chay())