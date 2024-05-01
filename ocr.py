import cv2
import numpy as np
import pytesseract
import matplotlib.pyplot as plt
from PIL import Image
import sys
from  extractor import KTPOCR

if __name__ == "__main__":  
    try:  
        ktppath = r"ktp.png"   
    except:
        ktppath = None
        print('Define your image path. Example: python ocr.py /path/of/image.jpg')
    if ktppath:
        ocr = KTPOCR(ktppath)
        word = ocr.to_json()
        print(word)