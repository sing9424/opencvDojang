import cv2
import numpy as np

# 이미지 읽기
src = cv2.imread('data/03.png')

# 노이즈 제거
dst1 = cv2.fastNlMeansDenoisingColored(src, None, 10, 10, 7, 21)

# BGR -> RGB 변환
dst = cv2.cvtColor(dst1, cv2.COLOR_BGR2RGB)

# 이미지 선명화
sharpening_mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpening_out = cv2.filter2D(dst1, -1, sharpening_mask)


# 결과 출력
cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('sharpening_out', sharpening_out)


cv2.waitKey()
cv2.destroyAllWindows()
