import cv2 as cv


def rescaleFrame(frame, scale = 0.5):
    # for Images, Videos, Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    return cv.resize(frame, dimensions)


def changeRes(width=250, height=250):
    # for Live Video only
    capture.set(3, width)
    capture.set(4, height)


img = cv.imread("cat.jpg")
cv.imshow("Cat", rescaleFrame(img, scale=0.2))
cv.waitKey(0)

capture = cv.VideoCapture("./cat.mp4")
# capture = cv.VideoCapture(0)
# changeRes()

while True:
    isTrue, frame = capture.read()
    if isTrue:
        resized_frame = rescaleFrame(frame)
        cv.imshow('Video', frame)
        cv.imshow('Resized Video', resized_frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()