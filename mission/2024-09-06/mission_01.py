import cv2, sys
import numpy as np
import matplotlib.pyplot as plt

src = cv2.imread('data/01.png', cv2.IMREAD_COLOR)
dst1 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)
dst = cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)

cv2.imshow('src', src)
cv2.imshow('dst', dst1)
cv2.waitKey()
cv2.destroyAllWindows()
