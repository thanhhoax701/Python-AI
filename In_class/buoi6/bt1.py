# Viết 1 CT chấp nhận đầu vào là 1 câu, đếm số chữ cái và chữ số trong đó. Giả sử đầu vào sau được cấp cho CT: hello worrld! 123 thì đầu ra sẽ là: Số chữ cái là: 20, Số chữ số là: 3
str = input("Nhập lẹ coi: ")

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

# Hoặc cái dưới cũng ra nữa

str = input("Nhap vao 1 cau: ")
countNum = 0; countLet = 0
for i in range(len(str)):
	if str[i].isdigit(): countLet+=1
	if str[i].isalpha(): countNum+=1
print("Số chữ cái là: ", countNum)
print("Số chữ số là: ", countLet)
