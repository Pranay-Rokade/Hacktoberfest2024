import pytesseract
import os
from PIL import Image
#path of the tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def convert():
    img = Image.open('Image.png')  #image
    text = pytesseract.image_to_string(img)
    print(text)
convert()
