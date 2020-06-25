from PIL import Image
import random
from random import randint
size = input()

message = []

for o in size:
    message.append(size)

for p in message:
    encript = [ord(c) for c in p]
column = []

img = Image.new( 'RGB', (len(encript), len(encript)), "black")
pixels = img.load() 

listofColours = []

for u in encript:
    listofColours.append(u)

for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixels[x,y] = (listofColours[0], random.randint(0, 255), random.randint(0, 255))
    listofColours.pop(0)

img.save(str(img.size[0] + img.size[1]) + ".png")