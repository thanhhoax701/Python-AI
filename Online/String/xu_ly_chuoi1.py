print(r"Haizz, \neu mot ngay nao do")

strA = "Họ và tên:Trần Thanh Hòa"
strB = "MSSV: B1908387"
strC = strA + "\n" + strB
print(strC)

a = "16/10/2001\n"
kq = a*3
print(kq)

#in : khi sử dụng toán tử này chỉ nhận đươc 1 trong 2 đáp án: true hoặc false
A = "Tran Thanh Hoa"
B = "a"
C = B in A
print(C)

# lấy kí tự ở vị trí thứ
str1 = "Hello my friend"
str2 = str1[2]
print(str2)

# lấy 1 kí tự từ vị trí cuối cùng đi vào
strA = "hello"
strB = strA[len(strA) - 1]
print(strB)

# cắt chuỗi
strD = "Hello.Friend"
strE = strD[None:5:1]
strF = strE in strD
print(strE)