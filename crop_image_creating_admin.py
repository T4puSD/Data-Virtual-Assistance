import cv2
import numpy as np
import os
import sys
import pyprind

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
bar = pyprind.ProgBar(500,bar_char = '#')


def detect(gray):
    faces= face_cascade.detectMultiScale(gray, 1.3, 5)
    roi_gray=gray
    for (x, y, w, h) in faces:
        cv2.rectangle(gray, (x, y), (x+w, y+h), (255,0,0) ,2)
        roi_gray =gray[y:y+h,x:x+w]
        #return roi_gray
    return roi_gray


Admin=input('Enter Name of Anything(object/person):')
try:
    print("Creating folder..."+Admin)
    os.makedirs('train_photos/'+Admin)
except Exception:
    print("Folder already exist!!!!")
    sys.exit()
    
cap = cv2.VideoCapture(0)
i=0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cropped = detect(gray)
    # Display the resulting frame
    cv2.imshow('frame',cropped)
    cv2.imwrite('./train_photos/'+Admin+'/'+Admin+'_'+str(i)+'.jpg',cropped)
    i+=1
    bar.update()
    if(i>500):
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
