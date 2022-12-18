class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    @classmethod
    def cap_nhat_suc_manh(cls, smanh):
        cls.suc_manh = smanh
sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)

SieuNhan.cap_nhat_suc_manh(40)

print(SieuNhan.suc_manh)
print(sieu_nhan_A.suc_manh)
