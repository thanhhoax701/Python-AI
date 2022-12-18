class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def __str__(self):
        return 'Day la {}, su dung {}'.format(self.ten, self.vu_khi)
    def __repr__(self):
        return 'ten: {}\nvu khi: {}\nmau sac: {}'.format(self.ten, self.vu_khi, self.mau_sac)

SN_A = SieuNhan('Sieu nhan Do', 'Kiem', 'Do')
print(SN_A)
print('%s' %SN_A)
print('%r' %SN_A)
