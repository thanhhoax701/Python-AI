class SieuNhan:
    so_thu_tu = 1
    suc_manh = 50
    def __init__(self, para_ten, para_vu_khi, para_mau_sac):
        self.ten = para_ten
        self.vu_khi = para_vu_khi
        self.mau_sac = para_mau_sac
        self.stt = SieuNhan.so_thu_tu
        SieuNhan.so_thu_tu += 1

sieu_nhan_A = SieuNhan("Sieu nhan do", "Kiem", "Do")
sieu_nhan_B = SieuNhan("Sieu nhan vang", "bua", "Vang")

print(sieu_nhan_A.stt)
print(sieu_nhan_B.stt)
print(SieuNhan.so_thu_tu)
