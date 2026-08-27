import cv2
import numpy as np

img1 = cv2.imread("D:\\personal\\zara\\berry01.jpeg")
img2 = cv2.imread("D:\\personal\\zara\\zara05.jpeg")

pts1 = np.float32([[100,100],[200,100],[100,200],[200,200]])
pts2 = np.float32([[120,120],[220,80],[150,250],[250,200]])

H, status = cv2.findHomography(pts1, pts2)

result = cv2.warpPerspective(img1, H, (img2.shape[1], img2.shape[0]))

cv2.imshow("Homography Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
