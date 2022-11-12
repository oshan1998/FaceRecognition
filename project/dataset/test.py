import cv2 as cv
import os
cascade = cv.CascadeClassifier("C:/Users/oshanchamara/Documents/ML_projects/FaceRecognition/FaceRecognition/project/dataset/haarcascade.xml")
name = str(input("input your name: "))
videoCapture = cv.VideoCapture(0)

assert cascade is not None
total=0
while videoCapture:
    print(total)
    _,img = videoCapture.read()
    orig = img.copy()
    assert img is not None
    
    key = cv.waitKey(1) & 0xFF
    if (key == ord('q')):
        break
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(gray,1.1,4)
    if key == ord('k'):
        p = os.path.sep.join(["./project/dataset", "{}.png".format(name+"_"+str(total).zfill(5))])
        total+=1
        cv.imwrite(p,orig)
    print("faces detected",len(faces))
    for (x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
    cv.imshow("video",img)
videoCapture.release()
cv.destroyAllWindows()

