import cv2
import math

img = cv2.imread('1.png')
pointsList = []

def mousePoints(event, x, y, flags, params):
    if event == cv2.EVENT_FLAG_LBUTTON:
        size = len(pointsList)
        if size != 0 and size % 3 != 0:
            cv2.line(img,tuple(pointsList[round((size-1)/3)*3]), (x,y),(0,0,255),2)
        cv2.circle(img,(x,y),5,(0,0,255),cv2.FILLED)
        pointsList.append([x,y])
    
def gradient(pt1,pt2):
    return (pt2[1]-pt1[1])/(pt2[0]-pt1[0])

def getangle(pointsList):
    pt1, pt2, pt3 = pointsList[-3:]
    m1 = gradient(pt1, pt2)
    m2 = gradient(pt1, pt3)
    angleR = math.atan((m2-m1)/(1+(m2*m1)))
    angleD = round(math.degrees(angleR))

    cv2.putText(img,str(angleD),(pt1[0]-40,pt1[1]-20), cv2.FONT_HERSHEY_COMPLEX,1.5,(255,0,0),2)

while True:
    if len(pointsList) % 3 == 0 and len(pointsList) != 0:
        getangle(pointsList)
    
    cv2.imshow('Image', img)
    cv2.setMouseCallback('Image', mousePoints)
    if cv2.waitKey(1) &  0xFF == ord('q'):
        pointsList = []
        img = cv2.imread('1.png')