class Car:
    # define class attribute
    loaixe = "oto"
    # thuộc tính đối tượng
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu
    # phương thức
    def dungxe(self, mucdich):
        return "{} dang dung xe de {}".format(self.tenxe,mucdich)
    def chayxe(self):
        return "{} dang chay tren duong".format(self.tenxe)
    def nomay(self):
        return "{} dang no may".format(self.tenxe)

toyota =  Car("Toyota", "Do", "Dien")
lamborghini = Car("Lamborghini", "Vang","Deisel")
porshe = Car("Porshe", "Xanh", "Gas")

print(toyota.dungxe("nap dien"))
print(lamborghini.chayxe())
print(porshe.nomay())
