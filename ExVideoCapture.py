# 이미지를 불러올 때는 imread()
# 동영상을 불러올 때는 VideoCapture()

import cv2, sys

fileName = 'data/vtest.avi'

# 동영상 파일 열기
cap = cv2.VideoCapture(fileName)

# 동영상의 해상도 width, height, frame수를 확인
print(cap.get(int(cv2.CAP_PROP_FRAME_WIDTH)))  # 동영상의 width정보를 가져오는 함수 'get_frame_width', int를 사용하여 정수로 가져와야함
print(cap.get(int(cv2.CAP_PROP_FRAME_HEIGHT))) # 동영상의 height정보를 가져오는 함수
print(cap.get(int(cv2.CAP_PROP_FRAME_COUNT))) # 

frameSize = cap.get(int(cv2.CAP_PROP_FRAME_WIDTH)), \
    cap.get(int(cv2.CAP_PROP_FRAME_HEIGHT))
print(frameSize)

# 동영상 이미지를 다 가져올 때까지 반복
# 영상을 한 프레임씩 가져옴
while(True):
    # retval : 동영상에서 이미지를 가져올때 정상 동작 했나?
    # frame은 이미지 한장
    # read() 함수 안에는 동영상 코덱도 함께 포함되어있어서 디코딩이 가능 (코덱 신경쓰지 않아도 됨)
    retval, frame = cap.read() # 동영상에서 한장의 이미지를 가져오기
    # frame.shape
    # retval가 양수가 아니면 while문 빠져나가기(종료)
    if not retval:
        break
    cv2.imshow('frame', frame)
    
    # 100ms 대기
    # 100초마다 while문이 돌고 key가 눌리면 break
    key = cv2.waitKey(100) # 이 동영상은 초당 10프레임 임.
    if key==27: # 키 입력이 ESC(27)이면 종료 (아스키 코드에 십진수 27이 ESC키임.)
        break
    
# 동영상을 열었으면, 닫아야한다.
if cap.isOpened():
    cap.release() # 열림해제
    
cv2.destroyAllWindows()
