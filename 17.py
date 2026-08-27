import cv2

img = cv2.imread(r"C:\PROGRAM\Open CV\Zara_009.png", 0)
sobel_x = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
cv2.imshow("Original", img)


cv2.imshow("Sobel X", sobel_x)
cv2.imwrite("sobel_x.jpg", sobel_x)

cv2.waitKey(0)
cv2.destroyAllWindows()
