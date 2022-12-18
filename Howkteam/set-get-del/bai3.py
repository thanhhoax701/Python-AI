class Kter:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
    @property
    def email(self):
        return self.ho + '-' + self.ten + '@kteam.com'
    @property
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)
    @ho_va_ten.setter
    def ho_va_ten(self, ten_moi):
        ho_moi, ten_moi = ten_moi.split(' ')
        self.ho = ho_moi
        self.ten = ten_moi
    @ho_va_ten.deleter
    def ho_va_ten(self):
        self.ho = None
        self.ten = None
        print('Da xoa')

kter_A = Kter("Tran", "Long")

kter_A.ho_va_ten = "Nguyen Giau"

print(kter_A.ho_va_ten)

del kter_A.ho_va_ten

print(kter_A.ho)
print(kter_A.ten)
