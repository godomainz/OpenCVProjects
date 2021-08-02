import cv2 as cv

# cap = cv.VideoCapture(0) Webcam
cap = cv.VideoCapture("Videos/Players.mp4")

while True:
    ret, frame = cap.read()
    cv.imshow("Frame", frame)

    if cv.waitKey(1) & 0xFF == ord("e"):
        break

cap.release()
cv.destroyAllWindows()