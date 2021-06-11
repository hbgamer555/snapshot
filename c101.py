import cv2
#cv2 is a python library which deals with using webcams and cameras
#captureobject=cv2.VideoCapture(0) this will open the webcam


#ret,frame=captureobject.read() it will read from your web cam
#cv2.imwrite("firstclick.jpg",frame)imwrite is used to save image on any storage device
#captureobject.release()to release the camera object
#cv2.destroyAllWindows()

def snapshot_create():
    captureobject=cv2.VideoCapture(0)
    ret,frame=captureobject.read()
    cv2.imwrite("firstsnap.jpg",frame)
    captureobject.release()
    cv2.destroyAllWindows()



snapshot_create()    
  