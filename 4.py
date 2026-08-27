import cv2

img = cv2.imread(r"D:\Program\OpenCV\zara_002_2026-02-26 at 9.40.10 AM.jpeg")

small = cv2.resize(img,None,fx=0.3,fy=0.3)
big = cv2.resize(img,None,fx=1,fy=1)

cv2.imshow("Small",small)
cv2.imshow("Big",big)
cv2.waitKey(0)
cv2.destroyAllWindows()
