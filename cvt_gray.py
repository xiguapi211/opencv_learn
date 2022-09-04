# author: ray
# date: 2022/9/4
import argparse
import cv2

parser = argparse.ArgumentParser(description='image file convert')
parser.add_argument('source', type=str, help='source file')
parser.add_argument('target', type=str, help='target file')

args = parser.parse_args()
source = args.source
target = args.target

img = cv2.imread(source)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite(target, img_gray)
print('Convert finished ~')
