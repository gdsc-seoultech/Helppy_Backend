import numpy as np
import cv2
import easyocr
import re

# ocr 모델 활성화
reader = easyocr.Reader(['ko','en'], gpu=True)

def ocr_model(data):
  encoded_img = np.frombuffer(data, dtype=np.uint8)
  img = cv2.imdecode(encoded_img, cv2.IMREAD_COLOR)
  result = reader.readtext(img, detail=0, paragraph=False, min_size=3, contrast_ths=0.1, adjust_contrast=0.5)
  recognized_text = ' '.join([r for r in result if r])
  recognized_text = re.sub(r'[^\w\s]', '', recognized_text)
  recognized_text = recognized_text.strip()
  if recognized_text:
    return recognized_text
  return "failed"
