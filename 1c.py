
import cv2

img = cv2.imread(r"D:\Program\OpenCV\Picture3.jpg",0)
edges = cv2.Canny(img,50,100)

cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
