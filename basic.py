import cv2 as cv

img = cv.imread("./cat.jpg")
cv.imshow("Cat", img)

# 1. Image Resizing
resized_img = cv.resize(img, (500,400), cv.INTER_AREA)
cv.imshow("Resized_Img", resized_img)

# 2. BGR to Gray-Scale
gray = cv.cvtColor(resized_img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# 3. Image Smoothing/ Blurring
blur = cv.GaussianBlur(resized_img, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# 4. Edges
edges = cv.Canny(blur, 125, 175)
cv.imshow("Edges", edges)

# 5. Dilating the image
dilated = cv.dilate(edges, (5,5), iterations=5)
cv.imshow("Dilated", dilated)

# 6. Eroding the image
eroded = cv.erode(dilated, (5,5), iterations=5)
cv.imshow("Eroded", eroded)

cv.waitKey(0)