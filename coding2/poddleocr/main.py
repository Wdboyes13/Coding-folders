from paddleocr import PaddleOCR
import cv2
img = cv2.imread("/Users/william/Downloads/IMG_4026.jpg")
img = cv2.resize(img, (640, 640))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
ocr = PaddleOCR(use_angle_cls=False, lang='en')
result = ocr.ocr(img)
print(result)