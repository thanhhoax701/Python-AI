class Car:
    # Constructor
    def __init__(self, hangxe, tenxe, mausac):
        self.hangxe = hangxe
        self.tenxe = tenxe
        self.mausac = mausac

    def chayxe(self):
        print ("{} dang chay tren duong".format(self. tenxe) )

    def dungxe(self, mucdich):
        print ("{} dang dung xe de {}".format(self.tenxe, mucdich))

class Toyota(Car):
    def __init__(self, hangxe, tenxe, mausac, nguyenlieu):
        super().__init__(hangxe, tenxe, mausac)
        self.nguyenlieu = nguyenlieu
    
    def chayxe(self):
        print("{} dang chay tren duong".format(self.tenxe))
    def dungxe(self, mucdich):
        print ("{} dang dung xe de {}".format(self.tenxe, mucdich))
        print ("{} chay bang {}".format(self.tenxe, self.nguyenlieu))
    def nomay(self):
        print("{} dang no may".format(self.tenxe))

toyota1 = Toyota("Toyota", "Toyota Hilux", "Do", "Dien")
toyota2 = Toyota("Toyota", "Toyota Yaris", "Vang","Deisel")
toyota3 = Toyota("Toyota", "Toyota Vios", "Xanh", "Gas")

toyota1.dungxe("nap dien")
toyota2.chayxe()
toyota3.nomay()