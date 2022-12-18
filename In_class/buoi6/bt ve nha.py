# Viết hàm cho phép kiểm tra 1 ký tự nhập vào có phải nguyên âm hay không. Nếu ký tự đó là nguyên âm, thì trả về 1, nếu không thì trả về 0

n=input("Nhập vào 1 ký tự: ")
while len(n)>1 or len(n)==0:
    n=input("Nhập lại: ")
if (n>='a' and n<='z') or (n>='A' and n<='Z'):
    if n in('a','o','e','u','i', 'A','O','E','U','I'):
        print(f"{n} là nguyên âm")
    else:
        print(f"{n} không là nguyên âm")


# Viết CT cho phép người dùng nhập vào 1 câu. Sau đó sd hàm đã viết ở câu 3 để đếm xem có bao nhiêu nguyên âm, phụ âm và ký tự đặc biệt trong câu đó
