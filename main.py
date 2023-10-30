import cv2
import numpy as np
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

imgQ = cv2.imread('Sources\Query_old.jpg')
cv2.imshow("Query_image", imgQ)
cv2.waitKey(0)