# Câu 1 : Viết chương trình cho phép người dùng nhập tên vào, sau đó in ra màn hình câu : “Hello” + tên, “ Welcome to Python”
ten = input("Nhap ten: ")
print("Hello " + ten + ", Welcome to Python")

# Câu 2 : Viết chương trình cho người dùng nhập vào số 0 <n < 10. Nếu n nằm ngoài khoản quy định thì yêu cầu người dùng nhập lại. Sau đó in ra màn hình kết quả của n + nn + nnn + nnnn (ví dụ : n = 2 thì in ra màn hình : 2 + 22 + 222 + 2222 = 2468)
n = int(input("Nhap vao so nguyen nho hon 10: "))
while n>10:
    n = int(input("Moi nhap lai: "))
kq = n + n+10*n + n+10*n+100*n + n+100*n+10*n+1000*n
n = str(n)
print(n + '+' + n*2 + '+' + n*3 + '+' + n*4 + '=' + str(kq))

# Câu 3 : Viết chương trình cho phép người dùng nhập vào 2 số a và b. Nếu b = 0 thì yêu cầu người dùng nhập lại cho đến khi b khác 0. In ra màn hình các kết quả của các phép toán sau : + - * / % **.
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
if (b==0):
    print("Moi nhap lai")
else:
    print(a+b, a-b, a*b, a/b, a%b, a**b)

# Câu 4 : Viết chương trình cho phép người dùng nhập vào bán kính hình tròn. In ra màn hình chu vi và diện tích tương ứng
r = int(input("Nhap vao ban kinh hinh tron: "))
cv = float(2*r*3.14)
s = float(r*r*3.14)
print("Chu vi: ",cv)
print("Dien tich: ",s)

# Cau 5: Viết chương trình tính giai thừa của số nguyên n được người dùng nhập vào từ bàn phím. Kiểm tra nếu n <0 thì yêu cầu người dùng nhập lại
n = int(input())
if n<0:
    print("Moi nhap lai")
else:
    ketQua = 1
    for i in range(1, n+1):
        ketQua *= i
    print(ketQua)

# Câu 6 : Viết hàm cho người dùng nhập vào 3 tham số a, b, c của phương trình ax2 + bx + c = 0 và in ra màn hình nghiệm của phương trình đó
import math

a = float(input('Nhap he so a: '),2)
while a == 0:
    if a == 0:
        print('Hay nhap lai he so a!')
        a = float(input('Nhap he so a: '))
b = float(input('Nhap he so b: '))
while b == 0:
    if b == 0:
        print('Hay nhap lai he so b!')
        b = float(input('Nhap he so b: '))
c = float(input('Nhap he so c: '))

delta = b * b - 4 * a * c
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print('Phuong trinh co 2 nghiem phan biet la:')
    print('x1 = ', x1)
    print('x2 = ', x2)
elif delta == 0:
    x = -b / (2 * a)
    print('Phuong trinh co nghiem kep la:')
    print('x1 = x2 = ', x)
else:
    print('Phuong trinh vo nghiem')

# Câu 7 : Viết chương trình tìm tất cả các số chia hết cho 7 nhưng không chia hết cho 5, nằm trong đoạn từ 5000 – 7000
for i in range(5000, 7000):
    if i % 7 == 0 and i % 5 != 0:
        print(i)

# Câu 8 : Viết chương trình chuyển số thập phân sang số nhị phân.
n=int(input("Nhap so thap phan: "))
x=n
k=[]
while (n>0):
    a=int(float(n%2))
    k.append(a)
    n=(n-a)/2
k.append(0)
string=""
for j in k[::-1]:
    string=string+str(j)
print("So nhi phan cua %d la %s"%(x, string))


# Câu 9: Viết chương trình tìm ước chung lớn nhất và bội chung nhỏ nhất của 2 số nguyên dương a và b được nhập vào từ bàn phím
def USCLN(a, b):
    if (b == 0):
        return a;
    return USCLN(b, a % b);
def BSCNN(a, b):
    return int((a * b) / USCLN(a, b));
a = int(input("Nhập số nguyên dương a = "));
b = int(input("Nhập số nguyên dương b = "));
print('USCLN: ', USCLN(a, b));
print('BSSCNN: ', BSCNN(a, b));

# Câu 10: Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n, với n được nhập vào từ bàn phím
import math
def isPrimeNum(n):
    if n < 2:
        return False
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i) == 0:
            return False
    return True
n = int(input("Nhap n = "))
print("Tat ca cac so nguyen to nho hon ", n, " la:")
sb = ""
if (n >= 2):
    sb = sb + "2" + " "
for i in range (3, n+1):
    if (isPrimeNum(i)):
        sb = sb + str(i) + " "
    i = i + 2
print(sb)

# Câu 11 : Viết chương trình liệt kê tất cả các số nguyên tố có 4 chữ số
import math

def isPrimeNumber(n):
    if (n < 2):
        return False
    # check so nguyen to khi n >= 2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
print ("Liet ke tat ca cac so nguyen to co 4 chu so:")
dem = 0
for i in range(1001, 9999):
    if (isPrimeNumber(i)):
        print(i)
        dem = dem + 1

# Câu 12 : Viết chương trình tính tổng của các chữ số của một số nguyên n. Nếu n nhỏ hơn 0 thì yêu cầu người dùng nhập lại. (ví dụ : n = 123 thì tổng là 1 + 2 + 3 = 6)
def totalDigitsOfNumber(n):
    total = 0
    while (n > 0):
        total = total + n % 10
        n = int(n / 10)
    return total

n = int(input("Nhap so nguyen duong n = "))
print("Tong cua", n , "là", totalDigitsOfNumber(n))

# Câu 13 : Viết chương trình tìm tất cả các số trong khoảng từ 1000 – 2000 sao cho tất cả các chữ số trong đó đều là số lẻ (ví dụ : 1157, 1597, 1375,…)
values = []
for i in range(1000, 2000):
    s = str(i)
    if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0) and (int(s[3])%2!=0):
        values.append(s)
print (",".join(values))

# Câu 14 : Viết chương trình tính 1/2 + 2/3 + 3/4 + 4/5 + … + n/(n+1) với số n được nhập từ bàn phím. Nếu n < 0 thì yêu cầu người dùng nhập lại.
n=int(input("Nhap so n >0: "))
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print (sum)

# Câu 15 : Viết chương trình tính dãy fibonacci f(n) với giá trị n được nhập từ bàn phím. Cách tính như sau : f(0) = 0, f(1) = 1, f(2) = f(1) + f(0), f(3) = f(2) + f(1), ….. , f(n) = f(n-1) + f(n-2)
def f(n):
    if n == 0:
        return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)
n=int(input("Nhap n: "))
print (f(n))
