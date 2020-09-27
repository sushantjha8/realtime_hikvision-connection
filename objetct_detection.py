from imageai.Detection import VideoObjectDetection

import imutils

from imutils.object_detection import non_max_suppression
import numpy as np
# read frame output
    
#import cv2
url="rtsp://admin:admin1234@169.254.28.64:554/Streaming/channels/301"
# url="rtsp://admin:admin1234@169.254.28.64:554/cam/realmonitor?channel=301&subtype=1"





cap = cv2.VideoCapture(url)
cap.set(cv2.CAP_PROP_FPS, 10)
print("read data ")
fps = int(cap.get(5))
print("fps:", fps)
hog = cv2.HOGDescriptor()

hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
i=0
frame_rate_divider = fps
try:
    while(True):
        ret, image = cap.read()
        
        if ret:
            if i % frame_rate_divider == 0:
                # frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
                
                #image = imutils.resize(image, width=min(400, image.shape[1]))
                orig = image.copy()

                print(ret)
                
                
                # draw the original bounding boxes
                # apply non-maxima suppression to the bounding boxes using a
                # fairly large overlap threshold to try to maintain overlapping
                # boxes that are still people
                
                    # detect people in the image
                (rects, weights) = hog.detectMultiScale(image, winStride=(4, 4),
                                                    padding=(8, 8), scale=1.05)
                rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
                
                pick = non_max_suppression(rects, probs=None, overlapThresh=0.8)
                print("w0001")
                

                # draw the final bounding boxes
                for (xA, yA, xB, yB) in pick:
                    cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
                # show the output images
                cv2.imshow("After NMS", image)
                i += 1
            else:
                i += 1
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
        


    #     # Our operations on the frame come here
    #     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #     read_frame(cap,detector)
    #     # Display the resulting frame
    #     cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
except:
    print ("cant read")
    pass
