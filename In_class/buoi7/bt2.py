# Định nghĩa 1 hàm có thể in dictionary chứa các key là số từ 1 đến 20 (gồm 1 và 20) và các giá trị bình phương của chúng
def printDict():
    d=dict() 
    for i in range(1,21): 
        d[i]=i**2 
        print (d) 
printDict()