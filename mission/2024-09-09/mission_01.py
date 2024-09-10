import cv2
import numpy as np

# 변수 초기화
points = []  # 찍힌 점들을 저장할 리스트
polygons = []  # 완성된 도형을 저장할 리스트
shift_pressed = False  # Shift 키의 상태

# 마우스 콜백 함수
def mouse_callback(event, x, y, flags, param):
    global points, polygons, shift_pressed

    # 원그리기
    if event==cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),50,(255,0,255),2)

    # Shift 키가 눌러진 상태
    if flags & cv2.EVENT_FLAG_SHIFTKEY:
        shift_pressed = True
        
        # 마우스 왼쪽 클릭 확인
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))  # 클릭한 좌표 추가
    
    # Shift 키가 떼어진 상태를 감지
    else:
        if shift_pressed:  # 이전에 Shift가 눌러졌었다면
            if len(points) > 2:  # 3개 이상의 점이 있을 때만 다각형을 생성
                polygons.append(points.copy())  # 도형을 polygons 리스트에 추가
            points = []  # points 리스트 초기화 (새로운 도형을 위해)
            shift_pressed = False  # Shift 상태 리셋

# 빈 이미지 생성
img = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# 윈도우 생성
cv2.namedWindow('img')
cv2.setMouseCallback('img', mouse_callback)

while True:
    # 점 찍은 도형 그리기
    for polygon in polygons:
        if len(polygon) >= 3:  # 3개 이상의 점일 때 다각형 그리기
            cv2.polylines(img, [np.array(polygon)], isClosed=True, color=(0, 255, 0), thickness=2)

    # 미리보기
    if len(points) > 1:
        cv2.polylines(img, [np.array(points)], isClosed=False, color=(255, 0, 0), thickness=1)
    
    # 이미지 출력
    cv2.imshow('img', img)

    # ESC를 눌러 종료
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC 키
        break
cv2.imwrite('mission_01.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 75])
# 윈도우 종료
cv2.destroyAllWindows()

