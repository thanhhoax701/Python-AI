# Viết chương trình tính giai thừa của 1 số nguyên dương n. Với n được nhập từ bàn phím #

# Cách 1: Không sử dụng đệ quy #

def tinhgiaithua(n):
    giai_thua = 1;
    if (n == 0 or n == 1):
        return giai_thua;
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i;
        return giai_thua;
 
n = int(input("Nhập số nguyên dương n = "));
print("Giai thừa của", n, "=", tinhgiaithua(n));

# Cách 2: Có sử dụng đệ quy #

n = int(input("Nhap n= "))
def giai_Thua(n):
    if n == 0:
        return 1
    return n * giai_Thua(n - 1)
print (giai_Thua(n))