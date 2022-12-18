# Đếm chữ hoa, chữ thường
str = input("Nhập lẹ coi: ")

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