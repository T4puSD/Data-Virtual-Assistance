
import cv2
import numpy as np
import os
import sys
import pyprind

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



def detect(gray):
    faces= face_cascade.detectMultiScale(gray, 1.3, 5)
    roi_gray=gray
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255,0,0) ,2)
        roi_gray =gray[y:y+h,x:x+w]
        #return roi_gray
    return roi_gray

cap = cv2.VideoCapture(0)
i=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cropped = detect(gray)
    cv2.imwrite('current_face.jpg',cropped)
    cv2.imshow('Log In',cropped)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        #print('exit')
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()

#import label_image
