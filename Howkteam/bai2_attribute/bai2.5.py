class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        print("Xin chao, ta la", self.ten)
        print("Suc manh cua ta la", self.suc_manh)
sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")

sieu_nhan_A.xin_chao()
