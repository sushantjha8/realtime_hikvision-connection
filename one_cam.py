import cv2
url="rtsp://192.168.0.105:8080/h264_ulaw.sdp"

cap = cv2.VideoCapture(url)
print("read data ")
while True:
# Capture frame-by-frame
    
    ret, frame = cap.read()
    print("frame read")

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    print(frame)
    print("frame read sucessfull")
    # Display the resulting frame
    #cv2.imshow('frame',frame





# When everything done, release the capture
