import cv2
import numpy as np

img = cv2.imread(r"C:\PROGRAM\Open CV\Zara_010.png")
kernel = np.array([[1,1,1],
                   [1,-8,1],
                   [1,1,1]])

sharp = cv2.filter2D(img, -1, kernel)

cv2.imshow("Sharpened", sharp)
cv2.imwrite("Sharpened_Image.jpg", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
