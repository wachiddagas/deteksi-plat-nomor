import cv2
import numpy as np

img = cv2.imread('dataset/sliced/circles.png', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Blue color rangle  169, 100, 100 , 189, 255, 255
lower_range = np.array([110, 50, 50])
upper_range = np.array([130, 255, 255])
mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('mask warna biru', mask)
cv2.imshow('image', img)

while (1):
    k = cv2.waitKey(0)
    if (k == 27):
        break

img_red = cv2.imread('dataset/sliced/circles.png', 1)
img_hsv=cv2.cvtColor(img_red, cv2.COLOR_BGR2HSV)

# lower mask (0-10)
lower_red = np.array([0,50,50])
upper_red = np.array([10,255,255])
mask0 = cv2.inRange(img_hsv, lower_red, upper_red)

# upper mask (170-180)
lower_red = np.array([170,50,50])
upper_red = np.array([180,255,255])
mask1 = cv2.inRange(img_hsv, lower_red, upper_red)

# join my masks
mask2 = mask0+mask1

# set my output img to zero everywhere except my mask
output_img = img_red.copy()
output_img[np.where(mask2==0)] = 0

# or your HSV image, which I *believe* is what you want
output_hsv = img_hsv.copy()
output_hsv[np.where(mask2==0)] = 0

cv2.imshow('mask warna merah', mask2)

#yellow range color
lower = np.array([22, 93, 0])
upper = np.array([45, 255, 255])

while (1):
    k = cv2.waitKey(0)
    if (k == 27):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()
