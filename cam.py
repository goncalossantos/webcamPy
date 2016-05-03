'''
Created on 3 May 2016

@author: goncalo
'''
import numpy as np
import cv2
import sys
cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

def getCam():
    cap = cv2.VideoCapture(0)
    return cap



def getImage(cap):
    
    
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    return (cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY),frame)


def detectFace(image,frame):
    faces = faceCascade.detectMultiScale(
    image,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30),
    flags=cv2.cv.CV_HAAR_SCALE_IMAGE
)
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        print "Found"
    return (image,frame)

  
def releaseCam(cap):  
    # When everything done, release the capture
    
    cap.release()
    cv2.destroyAllWindows()
    
    
if __name__ == '__main__':
    cam=getCam()
    while(True):
        img,frame=getImage(cam)
        img,frame=detectFace(img,frame)
        # Display the resulting frame
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    releaseCam(cam)
    