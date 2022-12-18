class Car:
    # define class attribute
    loaixe = "oto"
    # thuộc tính đối tượng
    def __init__(self, tenxe, mausac, nguyenlieu):
        self.tenxe = tenxe
        self.mausac = mausac
        self.nguyenlieu = nguyenlieu

toyota =  Car("Toyota", "Do", "Dien")
lamborghini = Car("Lamborghini", "Vang","Deisel")
porshe = Car("Porshe", "Xanh", "Gas")

print("Toyota la {}.".format(toyota.__class__.loaixe))
print("Lamborghini la {}.".format(lamborghini.__class__.loaixe))
print("Porshe la {}.".format(porshe.__class__.loaixe))

print("Xe {} co mau {}. {} la nguyen lieu van hanh.".format(toyota.tenxe, toyota.mausac, toyota.nguyenlieu))
print("Xe {} co mau {}. {} la nguyen lieu van hanh.".format(lamborghini.tenxe, lamborghini.mausac, lamborghini.nguyenlieu))
print("Xe {} co mau {}. {} la nguyen lieu van hanh.".format(porshe.tenxe, porshe.mausac, porshe.nguyenlieu))