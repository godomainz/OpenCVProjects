import cv2 as cv

img = cv.imread('Images/Ronaldo-1.jpg', 1)
cv.imshow('Image', img)
# Create a new file
cv.imwrite("Images_Write/Ronaldo_new.jpg", img)
cv.waitKey(0)