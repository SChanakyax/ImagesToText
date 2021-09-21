#https://www.youtube.com/watch?v=4DrCIVS5U3Y

import pytesseract as te
te.pytesseract.tesseract_cmd = r'C:\Software\TessaractManhem\tesseract.exe'
from PIL import Image

img = Image.open('imgTT3.jpg')
text = te.image_to_string(img)

print(text)