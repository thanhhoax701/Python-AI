# Viết chương triinhf cho người dùng nhập vào 2 số a và b. Điều kiện 20<a<50, b<10. In ra màn hình kết quả c=a/b. Viết Exception cho các trường hợp sau:
# - Giá trị a không nằm trong khoảng quy định
# - Giá trị b > 10
# - Giá trị b = 0
# In ra chữ Done! sau phép tính du có lỗi hay không


import sys
# randomList = ['a', 0, 2.0]
a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = a/b
while a>20 and a<50 and b<10:
    print(c)
else:
    if(a<=20 and a>=50 and b >=10):
        print("Gia tri a...")
