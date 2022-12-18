# Tạo class Human gồm các thuộc tính: họ tên, năm sinh, quê quán, nghề nghiệp. Các phương thức live(self, noicutru) và work(self, diachicoquan)
class Human:
    def __init__(self, hoTen, namSinh, queQuan, ngheNghiep):
        self.hoTen = hoTen
        self.namSinh = namSinh
        self.queQuan = queQuan
        self.ngheNghiep = ngheNghiep
        
    def live(self, noicutru):
        return "{} dang song o {}".format(self.hoTen,noicutru)
    def work(self, diachicoquan):
        return "{} dang lam {} tai truong {}".format(self.hoTen,self.ngheNghiep,diachicoquan)

human1 = Human("Tran Thanh Hoa", "2001", "Vinh Long", "Sinh Vien")

print(human1.live("Vinh Long"))
print(human1.work("Dai hoc Can Tho"))


# tạo thêm class Student kế thừa từ class Human bổ sung thêm 2 thuộc tính ngành học và msssv. Thêm phương thức study(self, Class)
class Student(Human):
    def __init__(self, hoTen, namSinh, queQuan, ngheNghiep, nganhHoc, mssv):
        super().__init__(hoTen, namSinh, queQuan, ngheNghiep)
        self.nganhHoc = nganhHoc
        self.mssv = mssv

    def live(self, noicutru):
        return "{} dang song o {}".format(self.hoTen,noicutru)
    def work(self, diachicoquan):
        return "{} dang lam {} tai truong {}".format(self.hoTen,self.ngheNghiep,diachicoquan)
    def study(self, Class):
        return "{} hoc nganh {} co mssv la {} dang hoc tai phong {}".format(self.hoTen,self.nganhHoc,self.mssv,Class)

student1 = Student("Tran Thanh Hoa", "2001", "Vinh Long", "Sinh Vien", "MMT&TTDL", "B1908387")

print(student1.study("P01"))
