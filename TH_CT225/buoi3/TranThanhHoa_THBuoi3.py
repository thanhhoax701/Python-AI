# Câu 1 : Viết chương trình khởi tạo lớp human gồm có những thông tin sau : họ tên, năm sinh, quê quán, nghề nghiệp. Viết phương thức :
#    - live(self, noicutru) : in ra màn hình người đó tên gì đang sống ở đâu
#    - work(self, diachicoquan) : in ra màn hình người đó tên gì đang làm nghề gì tại cơ quan nào (địa chỉ cơ quan)

class human:

    def __init__(self,hoten='',namsinh='',quequan='',nghenghiep=''):
        self.hoten=hoten
        self.namsinh=namsinh
        self.quequan=quequan
        self.nghenghiep=nghenghiep
    
    def live(self,noicutru):
        print("{} dang cu tru o {}".format(self.hoten,noicutru))
    
    def work(self,diachicoquan):
        print('{} dang lam nghe {} tai co quan {}'.format(self.hoten,self.nghenghiep,diachicoquan))

    def inh(self):
        print('Ho va ten: {}'.format(self.hoten))
        print('Nam sinh: {}'.format(self.namsinh))
        print('Que quan: {}'.format(self.quequan))
        print('Nghe nghiep: {}'.format(self.nghenghiep))

doge = human('Tran Thanh Hoa','2001','VL','sv')
doge.work('Dai hoc Can Tho')


# Câu 2 : Viết chương trình cho phép người dùng nhập vào số lượng người muốn nhập vào hệ thống. Tạo ra số lượng đối tượng thuộc lớp human tương ứng. 
# Sau đó tiến hành nhập thông tin, từng người (họ tên, năm sinh, ….) và lưu trong các biến thuộc lớp human.
# Ví dụ : 
#     Nhập số lượng người : 2
#     Nhập họ tên nguời thứ 1 : …..
#     Nhập năm sinh người thứ 1 : …
#     Nhập quê quán người thứ 1: …
#     Nhập nghề nghiệp người thứ 1: …
#     Nhập họ tên người thứ 2: …
#     …
# Sau đó in thông tin của các người dùng đó ra màn hình và sử dụng hàm work() để cho biết thông tin về nơi làm việc của những người đó với diachicoquan của từng người do sinh viên tự nhập vào.

c=int(input('Nhap so luong nguoi dung: '))
listhuman = []
for i in range (0,c):
    print('Nhap vao ho ten nguoi thu:',i+1)
    hoten=input()
    print('Nhap vao nam sinh nguoi thu:',i+1)
    namsinh=input()
    print('Nhap vao que quan nguoi thu:',i+1)
    quequan=input()
    print('Nhap vao nghe nghiep nguoi thu:',i+1)
    nghenghiep=input()
    doge=human(hoten,namsinh,quequan,nghenghiep)
    listhuman.append(doge)
for i in range (0,c):
    print('Thong tin cua nguoi thu:',i+1)
    listhuman[i].inh()
job = []
for i in range (0,c):
    print('Nhap vao dia chi co quan cua nguoi thu: ',i+1)
    diachicoquan=input()
    job.append(diachicoquan)
for i in range (0,c):
    listhuman[i].work(job[i])

class student(human):
    def __init__(self,hoten='',namsinh='',quequan='',nghenghiep='',mssv='',nganhhoc='',diemtb=0):
        super().__init__(hoten,namsinh,quequan,nghenghiep)
        self.nghenghiep='student'
        self.mssv=mssv
        self.nganhhoc=nganhhoc
        self.diemtb=int(diemtb)
    def inh(self):
        super().inh()
        print('MSSV: {}'.format(self.mssv))
        print('Nganh hoc: {}'.format(self.nganhhoc))
        print('Diem trung binh: {}'.format(self.diemtb))
    def study(self,Class):
        print('Sinh vien {} co mssv {} thuoc {} dang hoc tai phong {}'.format(self.hoten,self.mssv,self.nganhhoc,Class))

    def rank(self):
        kq=''
        if self.diemtb<4:
            kq='Loai Yeu'
        elif self.diemtb>=4 and self.diemtb<6:
            kq='Loai Trung Binh'
        elif self.diemtb>=6 and self.diemtb<8:
            kq='Loai Kha'
        else:
            kq='Loai Gioi'
        print('Sinh vien ten {} co MSSV {} voi diem trung binh {} duoc xep loai {}'.format(self.hoten,self.mssv,self.diemtb,kq))

    def inhkq(self):
        kq=''
        if self.diemtb<4:
            kq='Loai Yeu'
        elif self.diemtb>=4 and self.diemtb<6:
            kq='Loai Trung Binh'
        elif self.diemtb>=6 and self.diemtb<8:
            kq='Loai Kha'
        else:
            kq='Loai Gioi'
        print(kq)

# Câu 3 : Khai báo lớp Student là lớp con được kế thừa từ lớp Human với các thuộc tính được kế thừa từ lớp cha (thuộc tính nghề nghiệp được set mặc định thành “student”). 
# Ngoài ra lớp student còn có các thuộc tính riêng là MSSV, ngành học và điểm trung bình (điểm trung bình sử dụng thang điểm 10). Các phương thức : 
#     - Study(self, class) : cho biết sinh viên {tên} có {mssv} thuộc {ngành} đang học tại phòng học {class} nào
#     - Rank(self) : Cho biết thứ hạng của sv dựa vào điểm trung bình (ĐTB). 
#     ĐTB < 4 : Loại Yếu
#     4 <= ĐTB < 6 : Loại Trung bình
#     6 <= ĐTB < 8 : Loại Khá
#     8 <= ĐTB < 10 : Loại Giỏi
# In ra màn hình : Sinh viên {tên} có {MSSV} với điểm trung bình { ĐTB } được xếp loại {loại}

def nhapthongtin(self):
        print('Nhap vao ho ten (do dai khong qua 25 ky tu)')
        self.hoten=input()
        while (len(self.hoten)>26):
            print('Ho ten khong vuot qua 25 ky tu !')
            self.hoten=input()
        print('Nhap vao nam sinh:')
        self.namsinh=input()
        while (tontaichuoi(self.namsinh) or len(self.namsinh)!=4):
            while (tontaichuoi(self.namsinh)):
                print('Ban nhap khong phai so')
                self.namsinh=input()
            while (len(self.namsinh)!=4):
                print('Nam sinh co 4 chu so')
                self.namsinh=input()
        print('Nhap que quan: ')
        self.quequan=input()
        while (len(self.quequan)>50):
            print('Que quan khong vuot qua 50 ky tu !')
            self.quequan=input()
        print('Nhap vao MSSV')
        self.mssv=input()
        while (tontaichuoi(self.mssv) or len(self.mssv)>5):
            while (tontaichuoi(self.mssv)):
                print('MSSV chi chua cac ky tu so')
                self.mssv=input()
            while (len(self.mssv)>5):
                print('MSSV chi chua toi da 5 ky tu so')
                self.mssv=input()
        print('Nhap thong tin nganh hoc')
        self.nganhhoc=input()
        while (len(self.nganhhoc)>26):
            print('Nganh hoc khong vuot qua 40 ky tu !')
            self.nganhhoc=input()
        print('Nhap diem trung binh: ')
        self.diemtb=int(input())
        while (self.diemtb<0 or self.diemtb>10):
            print('Nhap diem trung binh: ')
            self.diemtb=int(input())

cheems=student()
cheems=student('Tran Thanh Hoa','2001','VL','sv','b1','MMT&TTDL','3')


# Câu 4 : Khai báo thông tin 2 sinh viên như sau : 
#     - SV1 : Tên : Lê Văn An, sinh năm 2005, quê Vĩnh Long, nghề nghiệp mặc định là sinh viên, MSSV = 12345, ngành CNTT, ĐTB = 7.6
#     - SV2 : Tên : Trần Văn Bình, sinh năm 2007, quê Trà Vinh, MSSV = 56789, Ngành Tài chính ngân hàng, ĐTB = 4.5
# Hãy in thông tin 2 sinh viên này ra màn hình và cho biết thứ hạng của 2 sinh viên này dựa trên điểm trung bình của họ. 

listsv= []
sv1=student('Le Van An',2005,'Vinh Long','',12345,'CNTT',7.6)
sv2=student('Tran Van Binh',2007,'Tra Vinh','',5678,'Tai Chinh Ngan Hang',4.5)
print('Thong tin sinh vien 1')
sv1.inh()
print('Thong tin sinh vien 2')
sv2.inh()
listsv.append(sv1)
listsv.append(sv2)
print('Thu tu xep hang sinh vien: ')
if (listsv[0].diemtb > listsv[1].diemtb):
    print('Sinh vien 1')
    print('Sinh vien 2')
else:
    print('Sinh vien 2')
    print('Sinh vien 1')


# Câu 5 : Viết Hàm cho phép người dùng nhập vào thông tin của MỘT sinh viên với những điều kiện như sau : 
#     - Họ tên có độ dài không quá 25 ký tự, Nếu dài hơn thì hiện ra thông báo “Ho ten khong vuot qua 25 ky tu !” và yêu cầu người dùng nhập lại 
#     - Năm sinh có độ dài đúng 4 ký tự số, Nếu có ký tự không phải số thì yêu cầu người dùng nhập lại. 
#     Nếu dài hơn 4 ký tự thì hiển thị thông báo “Nam sinh phai co 4 chu so ” và cũng yêu cầu người dùng nhập lại 
#     - Quê quán có độ dài không quá 50 ký tự, Nếu dài hơn thì hiện ra thông báo “Que quan khong vuot qua 50 ky tu !” 
#     và yêu cầu người dùng nhập lại 
#     - Nghề nghiệp mặc định là sinh viên ( Khai báo trực tiếp lúc khai báo lớp Sinh viên) nên không cần phải nhập 
#     - MSSV chứa tối đa 5 ký tự số, không chấp nhận các ký tự chữ cái. Nếu số ký tự dài hơn 5 thì yêu cầu người dùng nhập lại. 
#     Nếu có ký tự không phải số thì hiển thị thông báo : “MSSV chi chua cac ky tu so ! ” và yeu cầu người dùng nhập lại.
#     - Ngành học có độ dài không quá 40 ký tự, Nếu dài hơn thì hiện ra thông báo “nganh hoc 
#     khong vuot qua 40 ky tu !” và yêu cầu người dùng nhập lại 
# - Điểm trung bình phải lớn hơn 0 và nhỏ hơn 10. Nếu ĐTB nhỏ hơn 0 hoặc lớn hơn 10 thì yêu cầu người dùng nhập lại

# (Hàm này thêm vào cho khai báo class student ở bên trên)
def tontaichuoi(abc):
    kt=0
    for i in abc:
        if i.isalpha()==True:
            return True


# Câu 6 : Viết hàm cho phép người dùng nhập vào số lượng sinh viên cần Nhập thông tin (ví dụ : 3 ). 
# Sau đó sử dụng hàm đã viết ở câu 5 để cho người dùng nhập vào thông tin của từng sinh viên. 
# Sau đó in thông tin các sinh viên ra màn hình theo định dạng như sau :
#                                       Sinh vien 1
# ----------------------------------------------------------------------------------------------------------
# Ho ten : …….
# Nam sinh : ……
# Que quan : ……
# MSSV : ……
# Nganh Hoc : ……
# Diem trung binh : ……
# Xep Loai : ……
# ----------------------------------------------------------------------------------------------------------
#                                       Sinh vien 2
# ----------------------------------------------------------------------------------------------------------
# Ho ten : …….
# Nam sinh : ……
# Que quan : ……
# MSSV : ……
# Nganh Hoc : ……
# Diem trung binh : ……
# Xep Loai : ……
# ----------------------------------------------------------------------------------------------------------
#                                       Sinh vien 3
# ----------------------------------------------------------------------------------------------------------
# Ho ten : …….
# Nam sinh : ……
# Que quan : ……
# MSSV : ……
# Nganh Hoc : ……
# Diem trung binh : ……
# Xep Loai : ……

def indssv():
    listsv=[]
    c=int(input('Nhap vao so sinh vien can nhap: '))
    for i in range (0,c):
        print('Nhap vao thong tin cua sinh vien ',i+1)
        biden=student()
        biden.nhapthongtin()
        listsv.append(biden)
    for i in range (0,c):
        print('                                             Sinh vien ',i+1)
        print('----------------------------------------------------------------------------------------------------------')
        listsv[i].inh()
        print('Xep loai: ',end='')
        listsv[i].inhkq()
        print('----------------------------------------------------------------------------------------------------------')
indssv()


# Câu 7 : Viết chương trình khởi tạo một lớp Exchange gồm có các thuộc tính sau : Serial, Date, Amount, ExchangeType. 
# Lớp này có 2 phương thức là PrintExchange(self) và CashUp(self). 2 phương thức này tạm thời chưa thực hiện chức năng gì cả. 

class Exchange():
    def __init__(self,Serial='',Date='',Amout='',ExchangeType=''):
        self.Serial=Serial
        self.Date=Date
        self.Amount=Amout
        self.Exchangetype=ExchangeType

    def PrintExchange(self):
        print('')

    def Cashup(self):
        print('')

    def nhap(self):
        print('Nhap vao Serial:')
        self.Serial=input()
        while tontaichuoi(self.Serial) or len(self.Serial)>5:
            print('Serial must be a Number with max length = 5')
            self.Serial=input()
        print('Nhap vao ngay giao dich:')
        self.Date=input()
        while (len(self.Date)>10):
            print('Date must be a string with max length = 10')
            self.Date=input()
        print('Nhap vao so luong:')
        self.Amount=input()
        while (tontaichuoi(self.Amount)):
            print('Amount must be a number')
            self.Amount=input()


# Câu 8 : Khai báo một Lớp tên là GoldExchange kế thừa từ lớp Exchange ở câu 7. 
# Ngoài những thuộc tính ở lớp cha ra thì lớp GoldExchange sẽ có thêm các thuộc tính là GoldType và UnitPrice. 
# GoldType chỉ có 3 loại là : “18k”, “24k”, “9999”. Các phương thức được tái định nghĩa như sau : 
#     - CashUp(self) : được tính bằng Amount * UnitPrice tương ứng với GoldType
#     - PrintExchange(self) : In ra màn hình thông tin của giao dịch với định dạng : 
#         Serial – Date – GoldType – UnitPrice – Amount – Cash Up = số tiền
#     Ví dụ : 134 – 11/11/2020 – 18k – 3.200.000 – 3 – Cash Up = 9.600.000

class GoldExchange(Exchange):
    def __init__(self, Serial='', Date='', Amout='', ExchangeType='',GoldType='9999',UnitPrice=''):
        super().__init__(Serial, Date, Amout, ExchangeType)
        while (GoldType not in ('18k','24k','9999')):
            print('Invalid CurrentType, Please try again')
            GoldType=input()
        self.GoldType=GoldType
        self.UnitPrice=UnitPrice
    def Cashup(self):
        return int(self.Amount)*int(self.UnitPrice)

    def PrintExchange(self):
        print('{} - {} - {} - {} - {} - Cash Up = {}'.format(self.Serial,self.Date,self.GoldType,self.UnitPrice,self.Amount,self.Cashup()))
    
    def nhap(self):
        super().nhap()
        if self.Exchangetype=='GoldExchange':
            print('1:18k , 2:24k , 3:9999')
            while True:
                try:
                    b = int(input("Please enter a number: "))
                    while (int(b)!=1 and int(b)!=2 and int(b)!=3):
                        print('You must choose correct gold type')
                        b=input()
                    break
                except ValueError:
                        print('You must choose correct gold type')
            if b==1:
                self.GoldType='18k'
            elif b==2:
                self.GoldType='24k'
            else:
                self.GoldType='9999'
        if self.Exchangetype=='GoldExchange':
            print('Nhap vao UnitPrice: ')
            self.UnitPrice=input()
            while (tontaichuoi(self.UnitPrice)):
                print('UnitPrice must be a number')
                self.UnitPrice=input()


# Câu 9 : Khai báo một Lớp tên là CurrencyExchange kế thừa từ lớp Exchange ở câu 7. Ngoài những thuộc tính của lớp cha ra thì lớp CurrencyExchange có thêm các thuộc tính là CurrencyType, 
# ExchangeRate và Action. CurrencyType chỉ nhận 3 loại tiền tệ là USD, EUR và AUD, 
# ExchangeRate là tỷ giá trao đổi tương ứng với loại tiền tệ và Action tương ứng với hành động 
# mua/bán. Nếu Action = 1 thì ta hiểu là giao dịch mua, ngược lại là giao dịch bán.
# Các phương thức của lớp này được khai báo như sau : 
#     - CashUp(self) : Nếu là giao dịch mua thì số tiền sẽ được tính bằng Amount * ExchangeRate
#      Nếu giao dịch là bán thì số tiền sẽ là Amount * ExchangeRate * 1.1
#     - PrintExchange(self) : In ra màn hình thông tin của giao dịch như sau : 
#     Sell/Buy Exchange : Serial – Date – CurrencyType – ExchangeRate – Amount – Cash Up = số tiền
# Ví dụ : 
#     Buy Exchange : 115 – 11/11/2020 – USD – 25.000 – 100 – Cash Up = 2.500.000

class CurrencyExchange(Exchange):
    def __init__(self, Serial='', Date='', Amout='', ExchangeType='',CurrentType='USD',ExchangeRate='',Action=''):
        super().__init__(Serial, Date, Amout, ExchangeType)
        while (CurrentType not in ('USD','AUD','EUR')):
            print('Invalid CurrentType, Please try again')
            CurrentType=input()
        self.CurrentType=CurrentType
        self.ExchangeRate=ExchangeRate
        if Action==1:
            Action='Buy'
        else:
            Action='Sell'
        self.Action=Action
    
    def Cashup(self):
        if self.Action=='Buy':
            return int(self.Amount)*int(self.ExchangeRate)
        else:
            return float(self.Amount)*float(self.ExchangeRate)*1.1
    
    def PrintExchange(self):
        print ('{} Exchange: {} - {} - {} - {} - Cash Up = {}'.format(self.Action,self.Serial,self.Date,self.CurrentType,self.ExchangeRate,self.Amount,self.Cashup()))

    def nhap(self):
        super().nhap()
        if self.Exchangetype=='GoldExchange':
            print('1:USD , 2:EUR , 3:AUD')
            while True:
                try:
                    c = int(input("Please enter a number: "))
                    while (int(c)!=1 and int(c)!=2 and int(c)!=3):
                        print('You must choose correct currency type')
                        c=input()
                    break
                except ValueError:
                        print('You must choose correct currency type')
            if c==1:
                self.CurrentType='USD'
            elif c==2:
                self.CurrentType='EUR'
            else:
                self.CurrentType='AUD'
        if self.Exchangetype=='CurrencyExchange':
            print('Nhap vao ExchangeRate: ')
            self.ExchangeRate=input()
            while (tontaichuoi(self.ExchangeRate)):
                print('ExchangeRate must be a number')
                self.ExchangeRate=input()   
        print('Nhap loai giao dich 1:Buy Currency, 2:Sell Currency')
        while True:
            try:
                d = int(input("Please enter a number: "))
                while (int(d)!=1 and int(d)!=2):
                    print('You must choose action with your currency')
                    d=input()
                break
            except ValueError:
                    print('You must choose action with your currency')
        if d==1:
            self.Action='Buy'
        else:
            self.Action='Sell'


# Câu 10 : Viết hàm cho phép người dùng nhập vào một giao dịch mà họ muốn với các yêu cầu như sau : 
#     • Nhập mã giao dịch (Serial) : Serial phải là một dãy số, không chấp nhận các ký tự chữ cái, 
# độ dài tối đa 5 ký tự. Nếu người dùng nhập vào dài hơn 5 ký tự hoặc có các ký tự không phải 
# số thì hiển thị thông báo “Serial must be a Number with max length = 5 ” và yêu cầu người dùng nhập lại.
#     • Nhập ngày giao dịch (Date) : Date là kiểu chuỗi với độ dài tối đa 10 ký tự. Nếu độ dài nhập 
# vào dài hơn thì hiển thị thông báo : “Date must be a string with max length = 10” và yêu cầu người dùng nhập lại.
#     • Nhập số lượng (Amount) : Amount phải là kiểu số và không chấp nhận các ký tự không phải 
# số. Không giới hạn độ dài. Nếu người dùng nhập vào không phải ký tự số thì hiển thị thông 
# báo : “Amount must be a number” và yêu cầu người dùng nhập lại.
#     • Nhập Loại Giao Dịch : Lúc này sẽ hiển thị 2 chọn lựa ra màn hình : “1: GoldExchange ; 
# 2 : CurrencyExchange. Người dùng sẽ chọn 1 trong 2 giá trị đó . Nếu giá trị nhập vào không 
# phải là 1 hoặc 2 thì hiển thị thông báo : “You must choose between 1 or 2” và yêu cầu người dùng nhập lại.
#     • Nếu loại giao dịch là 1 thì sẽ hiển thị 3 lựa chọn cho người dùng chọn : “1 : 18k , 2 : 24k , 3 : 9999”
#         Nếu người dùng nhập vào không phải là 1, 2 hoặc 3 thì hiển thị thông báo : “You must choose correct gold type ” và yêu cầu người dùng nhập lại.
#     • Nếu loại giao dịch là 2 thì sẽ hiển thị 3 lựa chọn cho người dùng chọn : “1 : USD , 2 : EUR , 3 : AUD”
#         Nếu người dùng nhập vào không phải là 1, 2 hoặc 3 thì hiển thị thông báo : “You must 
# choose correct currency type ” và yêu cầu người dùng nhập lại.
#     • Nhập đơn giá (UnitPrice / ExchangeRate) : đơn giá lúc này sẽ được lưuthành Unit Price hoặc Exchange Rate tùy theo loại giao dịch tương ứng . 
#         Đơn giá phải là kiểu số và không chấp nhận các ký tự không phải số. Không giới hạn độ dài. 
#         Nếu người dùng nhập vào không phải ký tự số thì hiển thị thông báo : “UnitPrice / ExchangeRate must be a number” và yêu cầu người dùng nhập lại.
#     • Nếu loại giao dịch là 2 thì sẽ hiển thị 2 lựa chọn cho người dùng “1 : Buy Currency , 2 : Sell Currency” 
#         Nếu người dùng nhập vào không phải là 1, hoặc 2 thì hiển thị thông báo : “You must choose 
#         action with your currency ” và yêu cầu người dùng nhập lại.
#     • Sau đó in thông tin của giao dịch lên màn hình tương ứng với loại giao dịch và thông tin nhập vào.


# Câu 11 : Viết chương trình cho phép người dùng nhập vào n giao dịch bằng cách sử dụng lại hàm 
# đã viết ở câu 10. Sau đó in ra màn hình các Giao dịch với định dạng như sau : (Mỗi loại giao dịch sẽ được in khác nhau tùy theo loại giao dịch)
# ----------------------------------------------------------------------------------------------------------
#                                         Exchange 1 
# ----------------------------------------------------------------------------------------------------------
# Serial – Date – GoldType – UnitPrice – Amount – Cash Up = số tiền
# ----------------------------------------------------------------------------------------------------------
#                                         Exchange 2 
# ----------------------------------------------------------------------------------------------------------
# Serial – Date – GoldType – UnitPrice – Amount – Cash Up = số tiền
# ----------------------------------------------------------------------------------------------------------
#                                         Exchange 3 
# ----------------------------------------------------------------------------------------------------------
# Sell/Buy Exchange : Serial – Date – CurrencyType – ExchangeRate – Amount – Cash Up = số tiền

listExchange= []
print('Nhap so giao dich: ')
doge=int(input())
for i in range (0,doge):
    print('Lan giao dich thu ',i+1)
    print('Nhap loai giao dich (1:GoldExchange) (2:CurrencyExchange)')
    while True:
        try:
            a = int(input("Please enter a number: "))
            while (int(a)!=1 and int(a)!=2):
                print('You must choose between 1 or 2')
                a=input()
            break
        except ValueError:
            print('You must choose between 1 or 2')
    if a==1:
        cheems=GoldExchange()
        cheems.Exchangetype='GoldExchange'
    else:
        cheems=CurrencyExchange()
        cheems.Exchangetype='CurrencyExchange'
    cheems.nhap()
    listExchange.append(cheems)
for i in range(0,len(listExchange)):
    print('----------------------------------------------------------------------------------------------------------')
    print('                                            Exchange ',i+1)
    print('----------------------------------------------------------------------------------------------------------')
    listExchange[i].PrintExchange()


# Câu 12 : Viết hàm để đếm số lượng giao dịch mỗi loại ở câu 11 và in ra màn hình với định dạng : 
#      “Total of Gold Exchange : …..
#       Total of Currency Exchange : …”

totalGold=0
totalCurrency=0
for i in listExchange:
    if i.Exchangetype=='GoldExchange':
        totalGold+=1
    else:
        totalCurrency+=1
print('Total of Gold Exchange: ',totalGold)
print('Total of Currency Exchange: ',totalCurrency)