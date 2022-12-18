class Kter:
    def __init__(self, ho, ten):
        self.ho = ho
        self.ten = ten
        self.email = ho + '-' + ten + '@kteam.com'
    def ho_va_ten(self):
        return '{} {}'.format(self.ho, self.ten)
kter_A = Kter("Tran", "Long")
print(kter_A.ho)
print(kter_A.ten)
print(kter_A.email)
print(kter_A.ho_va_ten())
