import numpy as np
import cv2

img = cv2.imread(r"D:\Program\OpenCV\Picture1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Gray", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
