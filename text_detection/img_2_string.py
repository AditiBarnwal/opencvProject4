import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
img = cv2.imread("l.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract
##############################################
##           Image to String           ##
##############################################
print(pytesseract.image_to_string(img))
cv2.imshow('img', img)
cv2.waitKey(0)