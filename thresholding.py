import cv2 as cv

img = cv.imread("./coin1.jpg")
# cv.imshow("Coin", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)

# simple thresholding
T, threshold = cv.threshold(blur, 125, 255, cv.THRESH_BINARY)
cv.imshow("Threshold", threshold)

# otsu's thresholding
T, ostu = cv.threshold(blur, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("Ostu", ostu)

print("Optimal threshold value estimated by Ostu's: {0}".format(T))

# adaptive thresholding
adaptive = cv.adaptiveThreshold(blur, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 3, 5)
cv.imshow("Adaptive", adaptive)

cv.waitKey(0)