# Với 2 list cho trước: [12,3,6,78,35,55,120] và [12,24,35,78,88,120,155], viết chương trình để tạo list có phần tử là giao cả 2 list đã cho
list1 = set([12,3,6,78,35,55,120])
list2 = set([12,24,35,78,88,120,155])
list1 &= list2
li = list(list1)
print (li)