import cv2
import numpy as np

img = cv2.imread(r"D:\Program\OpenCV\zara_003.png")

(h, w) = img.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 45, 1)
rot = cv2.warpAffine(img, M, (w, h))

cv2.imshow("Rotated Image", rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
