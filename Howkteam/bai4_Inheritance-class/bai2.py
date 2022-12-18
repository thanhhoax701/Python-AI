class SieuNhan:
    suc_manh = 50

class SieuNhanGao(SieuNhan):
    pass

gao_do = SieuNhanGao()
print(gao_do.suc_manh)


class SieuNhan:
    suc_manh = 50

class SieuNhanGao(SieuNhan):
    suc_manh = 40

gao_do = SieuNhanGao()
print(gao_do.suc_manh)
