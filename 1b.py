import cv2

img = cv2.imread(r"D:\Program\OpenCV\Picture2.jpg")
blur = cv2.GaussianBlur(img, (7,7), 0)

cv2.imshow("Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
