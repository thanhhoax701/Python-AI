# gan cho bien a gia tri bang 4, voi a la kieu so nguyen
a = 1 
b = "Thanh Hoa"
c = 1.1234567891234567

print(a)
print(b)
print(c)

# kieu du lieu cua a
print(type(a))
print(type(b))
print(type(c))

# lay toan bo noi dung cua thu vien decimal
# tu thu vien decimal -> import moi thu (*) vao
from decimal import*

# lay toi da 30 chu so phan nguyen va phan thap phan
getcontext().prec = 30

f = 10/3
print(f)
print(type(f))
d = Decimal(10)/3
print(d)
print(type(d))