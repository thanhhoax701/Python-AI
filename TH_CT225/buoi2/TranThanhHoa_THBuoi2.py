# Câu 1 : Viết chương trình nhận vào một câu do người dùng nhập, in ra màn hình số chữ cái và số chữ số có trong câu vừa nhập
str = input("Nhập vào 1 câu: ")
d={"numbers":0, "letters":0}
for c in str:
    if c.isdigit():
        d["numbers"]+=1
    elif c.isalpha():
        d["letters"]+=1
    else:
        pass
print ("Số chữ cái là:", d["letters"])
print ("Số chữ số là:", d["numbers"])

# Câu 2 : Viết chương trình nhận vào một câu do người dùng nhập, in ra màn hình số chữ hoa và số chữ thường có trong câu vừa nhập
str = input("Nhập vào 1 câu: ")
d={"upper case":0, "lower case":0}
for c in str:
    if c.isupper():
        d["upper case"]+=1
    elif c.islower():
        d["lower case"]+=1
    else:
        pass
print ("Chữ hoa:", d["upper case"])
print ("Chữ thường:", d["lower case"])

# Câu 3 : Viết chương trình nhận vào một câu do người dùng nhập. Chuyển câu đó từ ký tự thường thành ký tự in hoa và in ra màn hình.
str = input("Nhập vào 1 câu: ")
print ("Chữ hoa:", str.upper())

# Câu 4 : Viết một chương trình tìm tất cả các số trong đoạn 100 và 300 (tính cả 2 số này) sao cho tất cả các chữ số trong số đó là số chẵn. In các số tìm được thành chuỗi cách nhau bởi dấu phẩy, trên một dòng.
ds = []
for i in range (100,301):
    if i%2==0:
        ds.append(i)
print(ds)

# Câu 5 : Viết chương trình cho người dùng nhập vào một dãy số, cách nhau bởi dấu phẩy, lọc a các số lẻ từ dãy số đó và in nó ra màn hình. Ví dụ: người dùng nhập : 1, 5, 4, 10, 6, 3, 7 thì kết quả sẽ là 1, 5, 3, 7
values = input("Nhap day so, cach nhau boi dau phay: ")
a = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(a))

# Câu 6 : Khai báo một từ điển mà key là các số từ 1 – 20, và value là các giá trị bình phương của key tương ứng. In từ điển trên ra màn hình theo mẫu : Key-value
def printDict():
    d=dict() 
    for i in range(1,21): 
        d[i]=i**2 
    for (key,value) in d.items(): 
        print (key, "-",value) 
printDict()

# Câu 7 : Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 4, thứ 5 trong [12,24,35,70,88,120,155]
li = [12,24,35,70,88,120,155]
li = [x for (i,x) in enumerate(li) if i not in (0,4,5)]
print (li)

# Câu 8 : Với 2 list cho trước: [12,3,6,78,35,55,120] và [12,24,35,78,88,120,155], viết chương trình để tạo list có phần tử là giao của 2 list đã cho
list1 = set([12,3,6,78,35,55,120])
list2 = set([12,24,35,78,88,120,155])
list1 &= list2
li = list(list1)
print (li)

# Câu 9 : Viết chương trình tạo một list chứa giá trị bình phương của các số từ 1 – 20. In list đó ra màn hình trừ 5 giá trị đầu tiên.
def printList():
    li=list() 
    for i in range(1,21): 
        li.append(i**2) 
    print (li[5:]) 
printList()

# Câu 10 : Viết chương trình cho phép người dùng nhập vào một tuple gồm 7 giá trị số. Nếu giá trị người dùng nhập vào không phải số thì yêu cầu họ nhập lại. Sau đó tạo một tuple khác chứa các giá trị là số chẵn trong tuple của người dùng nhập vào.
list1 = []
list2 = []
i=0
while len(list1)<7:
    print('Nhap vao so thu ',i)
    a=input()
    while a.isdigit()==False:
        print('Nhap sai!!!!')
        a=input()
    list1.append(a)
    i=i+1
for i in list1:
    if int(i)%2==0:
        list2.append(i)
list2.sort()
tuple(list2)
print(list2)

# Câu 11 : Viết chương trình cho phép người dùng nhập vào một câu, sau đó đếm và in số lượng của từng ký tự trong câu đó. Ví dụ : Người dùng nhập “Hello” thì sẽ in ra màn hình : 
#   H : 1
#   e : 1
#   l : 2
#   o : 1
#   Gợi ý : dùng kiểu dữ liệu từ điển 
str = input("Nhap vao mot cau: ")
count={}
for i in str:
    if i in count:
        count[i] +=1
    else:
        count[i] = 1

for i in sorted(count, key=count.get, reverse=False):
    print(i, count[i])

# Câu 12 : Viết chương trình cho phép người dùng nhập vào một câu, và in nó ra màn hình theo thứ tự ngược lại. Ví dụ : Người dùng nhập “Hello” thì in ra sẽ là : “olleH”
str = input("Nhap vao mot cau: ")
new_str = list(str)
new_str.reverse()
new_str = ''.join(new_str)

print(new_str)

# Câu 13 : Viết chương trình cho phép người dùng nhập vào một chuỗi, và in ra màn hình một chuỗi mới được tạo thành bởi 2 ký tự đầu và 2 ký tự cuối của chuỗi vừa nhập vào. Nếu chiều dài chuỗi nhập vào nhỏ hơn 2 ký tự thì yêu cầu người dùng nhập lại. Ví dụ: Người dùng nhập “abcd1234” thì in ra sẽ là : “ab34”, Người dùng nhập “ab” thì in ra sẽ là : “abab”.
str = input("Nhap vao mot chuoi: ")
while len(str) < 2:
    str = input("Moi nhap lai: ")

print(str[0:2] + str[-2:])

# Câu 14 : Viết chương trình cho phép người dùng nhập vào 2 chuỗi. Tạo một chuỗi mới là ghép của 2 chuỗi cũ, cách nhau bởi dấu phẩy, và hoán đổi 2 ký tự đầu của 2 chuỗi đó.
# Ví dụ : 
#   Chuỗi 1 : abc
#   Chuỗi 2 : xyz
#   Chuỗi kết quả : xyc abz
a=list(input("Nhap vao chuoi 1: "))
b=list(input("Nhap vao chuoi 2: "))
temp=a[len(a)-1]
a[len(a)-1]=b[len(b)-1]
b[len(b)-1]=temp
a.append(",")
c=a+b
for i in c:
    print(i,end="")

# Câu 15 : Viết chương trình cho người dùng nhập vào một chuỗi. Thay thế ký tự trùng lặp của ký tự đầu tiên trong chuỗi đó bằng ký tự @. In chuỗi mới ra màn hình. Ví dụ : Người dùng nhập “abcabc” thì in ra sẽ là : “abc@bc”
a = input("Nhap vao mot chuoi: ")
a = list(a)
kt = 0
for i in range(0,len(a)):
    j = i+1
    while j<len(a) and kt<1:
        if a[i]==a[j]:
            a[j] = "@"
            kt=kt+1
        j=j+1
for i in a:
    print(i,end="")


