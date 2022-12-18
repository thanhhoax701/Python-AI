# Viết chương trình tìm ước số chung lớn nhất và bội số chung nhỏ nhất của 2 số nguyên dương #

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