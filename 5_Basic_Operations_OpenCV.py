import cv2 as cv

img = cv.imread("Images_Write/Ronaldo_new.jpg", 1)
cv.imshow("Image", img)
e = cv.waitKey()

if e == 27:
    cv.destroyAllWindows()
elif e == ord("s"):
    cv.imwrite("Images_Write/The-New-Ronaldo.jpg", img)
    cv.destroyAllWindows()