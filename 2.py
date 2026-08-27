import cv2
cap = cv2.VideoCapture(r"D:\Program\OpenCV\zara_001_2026-02-11 at 8.38.03 PM.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video", frame)
    cv2.waitKey(100)   

cap.release()
cv2.destroyAllWindows()
