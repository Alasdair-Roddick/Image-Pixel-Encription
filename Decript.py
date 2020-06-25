from PIL import Image
import itertools

x = input("Plaese enter file directory (including extenstion): ")

img = Image.open(x)
pixel = img.load()

code = []

finalcode = []

for x in range(img.size[0]):
    print(pixel[x,0])
    code.append(pixel[x,0])


for a_tuple in code:
    finalcode.append(a_tuple[0])

x = ''.join(chr(i) for i in finalcode)
print(x)

input()