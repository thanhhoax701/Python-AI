# Câu 1 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng một chiều gồm các giá trị : 1, 3, 5, 7, 9
# sau đó in mảng đó ra màn hình ( Gợi ý : numpy.array() )
import numpy as np
arr = np.array([1,3,5,7,9])
print(arr)


# Câu 2 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều gồm các giá trị của dòng thứ
# nhất: 1, 3, 5, 7, 9 và dòng thứ hai : 2, 4, 6, 8 ,10 sau đó in mảng đó ra màn hình ( Gợi ý : numpy.array() )
import numpy as np
arr = np.array([[1,3,5,7,9],[2,4,6,8,10]])
print(arr)


# Câu 3 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng gồm 10 giá trị 0 và sau đó cập nhật giá 
# trị thứ 6 thành số 13. In mảng đó ra màn hình (Gợi ý : numpy.zeros() )
import numpy as np
arr=np.zeros(10)
arr[5]=13
print(arr)


# Câu 4 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều với kích thước 5x5 mà giá trị
# các đường viền đều là số 1, giá trị các phần tử còn lại là 0. (Gợi ý : numpy.ones() )
import numpy as np
arr=np.ones((5,5))
for i in range (1,4):
    for j in range (1,4):
        arr[i][j]=0
print(arr)


# Câu 5 : Sử dụng thư viện Numpy, Hãy khởi tạo một mảng hai chiều với kích thước 3x3 mà giá trị
# các phần tử đều là 1. Sau đó thêm 1 đường viền bao bên ngoài theo cả 2 chiều với toàn giá trị 0 vào 
# mảng vừa rồi. In mảng kết quả ra màn hình (Gợi ý : numpy.ones() và numpy.pad())
import numpy as np
arr=np.ones((3,3))
arr=np.pad(arr,(1, 1), 'constant', 
                constant_values=(0, 0))
print(arr)


# Câu 6 : Sử dụng thư viện Numpy, Hãy khởi tạo mảng thứ nhất gồm các phần tử : [10, 20, 40, 60, 
# 70] và màng thứ 2 gồm các phần tử : [10, 30, 50, 60]. Hãy tìm các phần tử chung của 2 mảng và in 
# kết quả ra màn hình (Gợi ý : numpy.intersect1d() )
import numpy as np
arr1=np.array([10,20,40,60,70])
arr2=np.array([10,30,50,60])
arr3=np.intersect1d(arr1,arr2)
print(arr3)


# Câu 7 : Sử dụng thư viện Numpy, Hãy khởi tạo mảng A gồm các phần tử toàn số chẵn từ 1 đến 100
# (tính luôn số 100). In mảng A ra màn hình. (Gợi ý : numpy.linspace() )
import numpy as np
arr=np.linspace(2,100)
print(arr)


# Câu 8 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ đồ thị hàm số y = sin(x) với x chạy từ đoạn 
# -10 đến 10. (Gợi ý : numpy.linspace() và plt.scatter(), plt.show() )
import matplotlib.pyplot as plt
import numpy as np
import math
arr=np.linspace(-10,10,num=21)
arr2 = []
for i in range (-10,11):
    arr2.append(math.sin(i))
print(arr2)
plt.scatter(arr,arr2)
plt.show()


# Câu 9 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ đồ thị hàm số x3 – 2x2 + x + 5 với x chạy từ đoạn -5 đến 5. 
# (Gợi ý : numpy.linspace() và plt.scatter(), plt.show() )
import matplotlib.pyplot as plt
import numpy as np
import math
arr=np.linspace(-5,5,num=11)
arr2= [ ]
for i in range (-5,6):
    arr2.append(math.pow(i,3)-2*math.pow(i,2)+i+5)
plt.scatter(arr,arr2)
plt.show()


# Câu 10 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ đồ thị hàm số y = sin(x) và y = cos(x) trên 
# cùng một hình với x chạy từ đoạn -10 đến 10. Đặt tiêu đề là “Đồ thị hình sin và cos”, gán legend
# tương ứng và đặt ở vị trí tốt nhất. (Gợi ý : plt.plot(), plt.title(), plt.legend() ).Kết quả như hình bên 
# dưới :
import matplotlib.pyplot as plt
import numpy as np
arr=np.linspace(-10,10)
sinx=np.sin(arr)
cosx=np.cos(arr)
plt.plot(arr,sinx,label='sin')
plt.plot(arr,cosx,label='cos')
plt.title('Do thi hinh sin va cos')
plt.legend()
plt.show()


# Câu 11 : Sử dụng thư viện Numpy và matplotlib, Hãy vẽ 3 đồ thị hàm số y = sin(x), y = cos(x) và y = tan(x) 
# trong cùng 1 ảnh với 3 đồ thị khác nhau. Mỗi ảnh có tiêu đề riêng. Kết quả giống như hình bên dưới.
# ( Gợi ý : plt.subplots(), plt.plot(), plt.title() ). 
# Hai đồ thị Cos và Sin thì phần X hiển thị từ -10 đến 10, đồ thị Tan thì hiển thị X từ -1.5 đến 1.5. 
# Cả 3 Đồ thị thì có Y hiển thị trong khoảng từ -2 đến 2 (dùng : set_xlim(), set_ylim() ). 
# Mỗi đồ thị hiển thị bằng một màu khác nhau.
import matplotlib.pyplot as plt
import numpy as np
fig, (fig1, fig2, fig3) = plt.subplots(1,3)
x=np.linspace(-10,10)

ysin=np.sin(x)
ycos=np.cos(x)
ytan=np.tan(x)

fig1.plot(x,ysin,'b')
fig2.plot(x,ycos,'g')
fig3.plot(x,ytan,'r')

fig1.set_title('sin')
fig2.set_title('cos')
fig3.set_title('tan')

fig1.set_xlim(-10,10)
fig2.set_xlim(-10,10)
fig3.set_xlim(-1.5,1.5)

fig1.set_ylim(-2,2)
fig2.set_ylim(-2,2)
fig3.set_ylim(-2,2)


# Câu 12 : Viết chương trình cho phép đọc vào một ảnh, sau đó hiển thị ảnh đó ra màn hình 
from PIL import Image
im = Image.open('wallpaper.jpg')
im.show()


# Câu 13 : Viết chương trình cho phép đọc vào một ảnh, sau đó tạo một box có kích thước 200x200 
# tại vị trí bắt đầu ở điểm có tọa độ (100, 100). Cắt ảnh với box tương ứng và hiển thị ảnh ra màn hình
from PIL import Image
im = Image.open('wallpaper.jpg')
im = im.resize((200,200))
imgcrop=im.crop((0,0,100,100))
imgcrop.show()


# Câu 14 : Viết chương trình cho phép đọc vào một ảnh, xoay ảnh đó 180 độ, sau đó lưu ảnh lại với 
# tên là “anhchinhsua.jpg” và hiển thị ảnh mới ra màn hình
from PIL import Image
im = Image.open('wallpaper.jpg')
im.rotate(180).save('anhchinhsua.jpg')


# Câu 15 : Viết chương trình cho phép chuyển ảnh màu thành ảnh trắng đen, sau đó xoay ảnh trắng 
# đen 90 độ, lưu ảnh lại với tên “anhtrangden.jpg” và hiển thị ảnh mới ra màn hình.
from PIL import Image
im = Image.open('wallpaper.jpg')
im=im.convert('L').rotate(90).save('anhtrangden.jpg')
im = Image.open('anhtrangden.jpg')
im.show()