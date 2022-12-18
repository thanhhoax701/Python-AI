class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 40

gao_do = SieuNhanGao("Gao do", "Cung", "Do")
print(gao_do.__dict__)
print(gao_do.suc_manh)

######

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
        self.su_thu = para_su_thu

gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")
print(gao_do.__dict__)
print(gao_do.suc_manh)


###############

class SieuNhan:
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac

class SieuNhanGao(SieuNhan):
    suc_manh = 40
    def __init__(self, para_ten, para_vu_khi, para_mau_sac, para_su_thu):
        # doi luc nguoi ta cung co the
        # SieuNhan.__init__(para_ten, para_vu_khi, para_mau_sac)
        # nhung dung super van la chu yeu
        super().__init__(para_ten, para_vu_khi, para_mau_sac)
        self.su_thu = para_su_thu

gao_do = SieuNhanGao("Gao do", "Cung", "Do", "Su tu")
print(gao_do.__dict__)
print(gao_do.suc_manh)

