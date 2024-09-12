import cv2
import numpy as np
import os
from glob import glob

class DataAugmentation:
    def __init__(self, base_path='DataAug'):
        self.base_path = base_path
        self.org_path = os.path.join(self.base_path, 'org')
        self.resize_path = os.path.join(self.base_path, 'resize')
        self.rotate_path = os.path.join(self.base_path, 'rotate')
        self.hflip_path = os.path.join(self.base_path, 'hflip')
        self.vflip_path = os.path.join(self.base_path, 'vflip')

        # Ensure directories exist
        for path in [self.resize_path, self.rotate_path, self.hflip_path, self.vflip_path]:
            if not os.path.exists(path):
                os.makedirs(path)

    def get_image_list(self):
        file_names = glob(os.path.join(self.org_path, '*.jpg'))
        return file_names

    def resize(self, img, file_name):
        dsize = (224, 224)
        img_resize = cv2.resize(img, dsize, interpolation=cv2.INTER_AREA)
        cv2.imshow('resize', img_resize)

        filepath = os.path.join(self.resize_path, f"{file_name}_resize.jpg")
        cv2.imwrite(filepath, img_resize)
        print(f"Resized image saved to {filepath}")

        return img_resize

    def rotate(self, src, angle, file_name):
        h, w = src.shape[:2]
        center_pt = (w / 2, h / 2)
        rot = cv2.getRotationMatrix2D(center_pt, angle, 1)
        dst = cv2.warpAffine(src, rot, (w, h))

        filepath = os.path.join(self.rotate_path, f"{file_name}_rot_{angle}.jpg")
        cv2.imwrite(filepath, dst)
        print(f"Rotated image saved to {filepath}")

        return dst

    def hflip(self, img, file_name):
        flipped_img = cv2.flip(img, 1)
        filepath = os.path.join(self.hflip_path, f"{file_name}_hflip.jpg")
        cv2.imwrite(filepath, flipped_img)
        print(f"Horizontally flipped image saved to {filepath}")

        return flipped_img

    def vflip(self, img, file_name):
        flipped_img = cv2.flip(img, 0)
        filepath = os.path.join(self.vflip_path, f"{file_name}_vflip.jpg")
        cv2.imwrite(filepath, flipped_img)
        print(f"Vertically flipped image saved to {filepath}")

        return flipped_img

    def crop(self, img, scale):
        h, w = img.shape[:2]
        new_w = int(w * scale)
        new_h = int(h * scale)
        start_x = (w - new_w) // 2
        start_y = (h - new_h) // 2
        end_x = start_x + new_w
        end_y = start_y + new_h
        cropped_img = img[start_y:end_y, start_x:end_x]
        return cropped_img

    def process_images(self):
        cv2.namedWindow('img')
        file_names = self.get_image_list()

        for file_path in file_names:
            src = cv2.imread(file_path)
            if src is None:
                print(f'Error: {file_path}')
                continue

            file_name = os.path.splitext(os.path.basename(file_path))[0]

            # Example processing steps
            rotated_img = self.rotate(src, 30, file_name)
            crop_img = self.crop(rotated_img, 0.7)
            resize_crop_img = self.resize(crop_img, file_name)
            # hflip_img = self.hflip(resize_crop_img, file_name)
            # vflip_img = self.vflip(resize_crop_img, file_name)

            cv2.imshow('src', resize_crop_img)
            cv2.waitKey()

        cv2.destroyAllWindows()

if __name__ == "__main__":
    data_augmenter = DataAugmentation()
    data_augmenter.process_images()

