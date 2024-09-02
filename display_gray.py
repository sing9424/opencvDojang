# plt.imshow함수에서 interpolation옵션
# camp은 이미지가 컬러일 경우 cmap지정을 안해도 컬러로 출력
# camp = "gray"

import cv2, sys
from matplotlib import pyplot as plt

fileName = 'data/cat.jpg'

imgGray = cv2.imread(fileName, cv2.IMREAD_GRAYSCALE)
print(imgGray.shape)

plt.axis('off')
plt.imshow(imgGray, cmap='gray')
plt.show()