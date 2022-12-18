# Viết chương trình in list sau khi đã xóa số ở vị trí thứ 0, thứ 4, thứ 6 trong [12,24,35,70,88,120,155]
li = [12,24,35,70,88,120,155]
a = [x for i,x in enumerate(li)if i%2!=0]
print (a)