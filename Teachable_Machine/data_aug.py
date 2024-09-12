# 1. 배경 : 흰색 책상, 우드 테이블
# 2. 데이터 증식 조건 
#    2.0 스마트폰으로 사진을 촬영 후 이미지 크기를 줄여주자. (이미지크기는 224x224)
#        대상물 촬영을 어떻게 해야할지 고민
#    2.1 rotate : 회전(10~30도)범위 안에서 어느 정도 각도를 넣어야 인식이 잘되는가?
#    2.2 hflip, vflip : 도움이 되는가? 넣을 것인가?
#    2.3 resize, crop : 가능하면 적용해 보자.
#    2.4 파일명을 다르게 저장 cf) jelly_wood.jpg, jelly_white.jpg
#        jelly_wood_rot_15.jpg, jelly_wood_hflip.jpg,jelly_wood_resize.jpg 
#    2.5 클래스 별로 폴더를 생성
#    2.6 데이터를 어떻게 넣느냐에 따라 어떻게 동작되는지 1~2줄로 요약

# 구성순서
# 1. 이미지를 촬영한다.
# 2. 이미지를 컴퓨터로 복사, resize한다.
# 3. 육안으로 확인, 이렇게 사용해도 되는가?
# 4. 함수들을 만든다. resize, rotate, hfilp, vfilp, crop, 
#    원본파일명을 읽어서 파일명을 생성하는 기능은 모든 함수에 있어야한다. (함수) -모듈
# 5. 단일한수들 검증
# 6. 함수를 활용해서 기능 구현
# 7. 테스트(경우의 수)
# 8. 데이터셋을 teachable machine사이트에 올려서 테스트
# 9. 인식이 잘 되는 케이스를 분석하고 케이스 추가 1~8에서 구현된 기능을 이

import cv2, sys
import numpy as np
import os
from glob import glob

# RESIZE_EN = True
# ROTATE_EN = True

def getImageList():
    # 현재경로 불러오기
    dataPath = os.path.join(os.getcwd(),'DataAug')
    dataOrg = os.path.join(dataPath, 'org')
    fileNames = glob(os.path.join(dataOrg,'*.jpg'))

    return fileNames

def resize(img, file_name):
    dsize = (224, 224)
    # 스마트폰으로 촬영된 이미지를 224x224로 변경
    # Resize시에는 interpolation을 무엇을 할 지도 중요
    img_resize = cv2.resize(img,dsize, interpolation=cv2.INTER_AREA)
    cv2.imshow('resize',img_resize)

    dataPath = os.path.join(os.getcwd(),'DataAug')
    folder_name = os.path.join(dataPath, "resize")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filepath = os.path.join(folder_name, f"{file_name}_resize.jpg" )
    cv2.imwrite(filepath,img_resize)
    print(f"resized image saved to {filepath}")

    return img_resize

def rotate(src, angle, file_name):
    h,w = src.shape[:2]
    centerPt = (w/2, h/2)
    rot = cv2.getRotationMatrix2D(centerPt, angle, 1)
    dst = cv2.warpAffine(src, rot, (w,h))

    dataPath = os.path.join(os.getcwd(),'DataAug')
    folder_name = os.path.join(dataPath, "rotate")
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    filepath = os.path.join(folder_name, f"{file_name}_rot_{angle}.jpg")

    cv2.imwrite(filepath, dst) 
    print(f"rotate image saved to {filepath}")

    return dst

def hflip(img, file_name):
    # 폴더 생성
    dataPath = os.path.join(os.getcwd(), 'DataAug')
    folder_name = os.path.join(dataPath, "hflip")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 좌우 반전 (수평 반전)
    flipped_img = cv2.flip(img, 1)

    # 파일 경로 설정 및 저장
    filepath = os.path.join(folder_name, f"{file_name}_hflip.jpg")
    cv2.imwrite(filepath, flipped_img)
    print(f"Horizontally flipped image saved to {filepath}")
    
    return flipped_img

def vflip(img, file_name):
    # 폴더 생성
    dataPath = os.path.join(os.getcwd(), 'DataAug')
    folder_name = os.path.join(dataPath, "vflip")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # 상하 반전 (수직 반전)
    flipped_img = cv2.flip(img, 0)

    # 파일 경로 설정 및 저장
    filepath = os.path.join(folder_name, f"{file_name}_vflip.jpg")
    cv2.imwrite(filepath, flipped_img)
    print(f"Vertically flipped image saved to {filepath}")
    
    return flipped_img

def crop(img, scale):
    h, w = img.shape[:2]  # 이미지의 높이와 너비

    # scale에 따른 crop 크기 계산
    new_w = int(w * scale)
    new_h = int(h * scale)

    # 중앙을 기준으로 자를 좌표 계산
    start_x = (w - new_w) // 2
    start_y = (h - new_h) // 2
    end_x = start_x + new_w
    end_y = start_y + new_h

    # 이미지 crop (scale 비율만큼 잘라내기)
    cropped_img = img[start_y:end_y, start_x:end_x]

    return cropped_img

cv2.namedWindow('img')
fileNames = getImageList()

for filePath in fileNames:
    # 이미지 불러오기
    src = cv2.imread(filePath)
    if src is None:
        print(f'error: {filePath}')
        continue

    file_name = os.path.splitext(os.path.basename(filePath))[0]

    # 이미지 Resize 적용 및 저장
    # resized_img = resize(src, file_name)
    # cv2.imshow('res_img', resized_img)
    
    # 이미지 Rotate 적용 및 저장 (예: 15도 회전)
    # rotated_img = rotate(src, 15, file_name)
    rotated_img = rotate(src, 30, file_name)
    crop_img = crop(rotated_img, 0.7)
    resize_crop_img = resize(crop_img, file_name)
    # hflip_img = hflip(resized_img, file_name)
    # vflip_img = vflip(resized_img, file_name)

    # cv2.imshow('src',src)
    #cv2.imshow('src',hflip_img)
    # cv2.imshow('src',vflip_img)
    cv2.imshow('src',resize_crop_img)
    cv2.waitKey()

cv2.destroyAllWindows()
