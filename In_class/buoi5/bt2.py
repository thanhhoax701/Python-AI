# Viết hàm cho người dùng nhập vào 3 tham số a, b, c của phương trình ax2 + bx + c =0 và in ra màn hình nghiệm của phương trình đó #

import math

a = float(input('Nhap he so a: '))
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
    