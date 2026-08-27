import cv2

img = cv2.imread(r"C:\PROGRAM\Open CV\zara_012.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

gradient = cv2.subtract(gx, gy)
cv2.imshow("Original", img)
cv2.imshow("Gradient Mask", gradient)
cv2.imwrite("sharpened_image3.jpg", gradient)

cv2.waitKey(0)
cv2.destroyAllWindows()
