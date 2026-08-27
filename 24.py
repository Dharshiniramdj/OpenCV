import cv2
import numpy as np

img = cv2.imread(r"C:\PROGRAM\Open CV\zara_012.png")

# Create blurred image
kernel = np.ones((3, 3), np.float32) / 9
blur = cv2.filter2D(img, -1, kernel)

# High-boost filtering
boost = 1.5
mask = img.astype(np.float32) - blur.astype(np.float32)
sharp = img.astype(np.float32) + boost * mask

# Convert values to 0-255
sharp = np.clip(sharp, 0, 255).astype(np.uint8)

cv2.imshow("Original", img)
cv2.imshow("Blur", blur)
cv2.imshow("High Boost", sharp)

cv2.imwrite("sharpened_image.jpg", sharp)

cv2.waitKey(0)
cv2.destroyAllWindows()
