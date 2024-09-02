# 이미지 불러오기 : 'imageRead.py' 파일과 동일
# opencv 패키지의 특성과 matplotlib 패키지의 특성의 차이를 이해
# 이미지 출려하기 : cv2.imshow() -> plt.imshow()

import cv2
import sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

imgRGB = cv2.imread(fileName)

if imgRGB is None:
    sys.exit("Image load is failed")
    

# << opencv 모듈과 matplotlib 모듈 순서의 차이점!! >>
# opencv 모듈은 이미지를 읽어올대 컬러 스페이스의 순서 B,G,R
# 컬러 스페이스(채널순서)를 바꿔주는 함수

imgRGB = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2RGB)  # 채널순서를 bgr에서 rgb로 바꿔주는 함수

# matplotlib은 R,G,B 순서로 사용

plt.imshow(imgRGB)
# matplotlib의 imshow에서 눈금을 표시 안함
# plt.axis('off')
plt.show()