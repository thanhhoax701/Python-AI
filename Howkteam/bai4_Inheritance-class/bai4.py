class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
    def xin_chao(self):
        print("Xin chao, ta la", self.ten)
    def show_suc_manh(self):
        print("Suc manh cua ta la", self.suc_manh)

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_su_thu
    def show_suc_manh(self):
        print("Suc manh cua ta la", self.suc_manh)
        print("Su dung su thu", self.su_thu)

sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")

sieu_nhan_A.xin_chao()
gao_do.xin_chao()

sieu_nhan_A.show_suc_manh()
gao_do.show_suc_manh()
