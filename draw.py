import cv2 as cv
import numpy as np


blank = np.zeros((450,450,3), dtype='uint8')
cv.imshow("Blank", blank)

# 1. Paint the image
blank[200:300, 300:400] = 0,255,0
cv.imshow("Green", blank)

# 2. Draw a rectangle
blank = np.zeros((450,450,3), dtype='uint8')
cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=2)
cv.imshow("Rectangle", blank)

# 3. Draw a Circle
blank = np.zeros((500,500,3), dtype='uint8')
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 50, (0,0,255), thickness=cv.FILLED)
cv.imshow("Circle", blank)

# 4. Draw a Line
blank = np.zeros((450,450,3), dtype='uint8')
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
cv.imshow("Line", blank)

# 5. Put Text
blank = np.zeros((500,500,3), dtype='uint8')
cv.putText(blank, "Hello! This is Hamza Sabir", (0, blank.shape[1]//2), cv.FONT_HERSHEY_COMPLEX
                                                , 1, (255,0,0), 2)
cv.imshow("Text", blank)

cv.waitKey(0)