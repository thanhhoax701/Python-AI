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

kter_A = Kter("Tran", "Long")

kter_A.ho_va_ten = "Nguyen Giau" # day la argument cho parameter ten_moi

print(kter_A.ho_va_ten)
