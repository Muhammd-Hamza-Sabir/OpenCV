import cv2 as cv

img = cv.imread("cat.jpg")

cv.imshow("Image", img)
cv.waitKey(0)

capture = cv.VideoCapture("./cat.mp4")

while True:
    isTrue, frame = capture.read()

    if isTrue:    
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()