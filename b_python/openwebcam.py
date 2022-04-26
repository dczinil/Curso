import  cv2, time
cap = cv2.VideoCapture(0)
check, frame=video.read()


print(check)
print(frame)




if not cap.isOpened():
    raise IOErorr("Cannot open WebCam")
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.waitKey(1)
    if c == 27:
        break
cap.release()
cv2.destroyAllWindows()