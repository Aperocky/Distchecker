import numpy as np
import cv2
import os, sys

# Written by Rocky Li @ aperocky@gmail.com on July 17, 2018
# With Goodwell.

def draw_circle(event,x,y,flags,param):
    global mouseX,mouseY, record
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        mouseX,mouseY = x,y
        record.append((x,y))
        print("You clicked on %d, %d" % (x, y))

def calclength(record):
    # between 1st click and 2nd click.
    def dist(p1, p2):
        return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

    roadside = dist(record[0], record[1])
    expdistance = dist(record[0], record[2])
    return roadside, expdistance
    
if __name__ == "__main__":
    fname = sys.argv[1]
    img = cv2.imread(fname)
    print(" Reading image.. \n Please make sure that you click roadside, gravel, experimenter's feet, in that order \n Written By Rocky Li \n")
    record = []
    mywindow = cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_circle)

    while(True):
        cv2.imshow('image',img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord("c"):
            break
        if len(record) >= 3:
            break

    print("This is the pixel distance")
    r, d = calclength(record)
    print(r, d)
    print("This is the calculated Distance")
    dist = d/r*7
    print("Experimenter are %.02f feet away" % dist)
    cv2.destroyAllWindows()   