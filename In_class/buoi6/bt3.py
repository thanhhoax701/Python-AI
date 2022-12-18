# Viết chương trình cho phép nhập vào 1 số nguyên n nhỏ hơn 10, nếu lớn hơn 10 thì yêu cầu người dùng nhập lại. Sau đó in ra màn hình kết quả của n + nn + nnn
n=int(input("Nhap vao so nguyen nho hon 10: "))
kq=0
if(n>10):
    input("Moi nhap lai: ")
else:   
    kq=n+10*n+n+100*n+10*n+n
print(kq)