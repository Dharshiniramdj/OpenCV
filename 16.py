import cv2

img = cv2.imread(r"C:\PROGRAM\Open CV\zara_003.png", 0)
edges = cv2.Canny(img, 100, 200)

cv2.imshow("Canny Edges", edges)
cv2.imwrite("Edges.jpg", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
