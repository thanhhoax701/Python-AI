from rembg import remove
from PIL import Image
input_path = 'D:\Learn-Programming\Python\Tool\pictures\1.jpg'
output_path = 'D:\Learn-Programming\Python\Tool\pictures\ouput.png'
input = Image.open(input_path)
output = remove(input)
output.save(output_path)