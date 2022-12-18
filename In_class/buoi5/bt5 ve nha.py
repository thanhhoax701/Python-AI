# Viết chương trình liệt kê tất cả các số nguyên tố nhỏ hơn n. Số nguyên dương n được nhập từ bàn phím

import math

def isPrimeNum(n):
    if n < 2:
        return False
    tg = int(math.sqrt(n))
    for i in range(2, tg + 1):
        if (n % i) == 0:
            return False
    return True

n = int(input('Nhap so nguyen duong n = '))
print('Cac so nguyen to nho hon ', n, ' la:')
if n >= 2:
    print(2)
    for i in range(3, n + 1):
        if isPrimeNum(i):
            print(i)
        i = i + 2

