import cv2
import numpy as np

img = cv2.imread(r"C:\PROGRAM\Open CV\zara_003.png")

src = np.float32([
    [0, 0],
    [img.shape[1]-1, 0],
    [0, img.shape[0]-1],
    [img.shape[1]-1, img.shape[0]-1]
])

dst = np.float32([
    [50, 50],
    [img.shape[1]-50, 50],
    [50, img.shape[0]-50],
    [img.shape[1]-50, img.shape[0]-50]
])

H, _ = cv2.findHomography(src, dst)

result = cv2.warpPerspective(
    img, H, (img.shape[1], img.shape[0])
)

cv2.imshow("Original", img)
cv2.imshow("DLT Transformed", result)

cv2.imwrite("DLT_Transformed.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
