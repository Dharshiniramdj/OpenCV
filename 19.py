import cv2

img = cv2.imread(r"C:\PROGRAM\Open CV\Zara_009.png", 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

edges = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)
cv2.imshow("Original", img)
cv2.imshow("Sobel XY", edges)
cv2.imwrite("Edge_detection.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
