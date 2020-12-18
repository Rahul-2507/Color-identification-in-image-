#RAHUL MISHRA

#sparks foundation

#import liblraries
import cv2 as cv
import numpy as np
import pandas as pd

#read image
img = cv.imread('D:\sparks\colorpic.jpg')

#declare variables
clicked = False
r = g =b= xpos =ypos = 0

#read data from csv file
index = ["colors","color_name","hex","R","G","B"]
data = pd.read_csv('colors.csv', names=index, header=None)


#calculate minimum distance from all colors and get most matching colors
def getcolorname(R,G,B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R- int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = data.loc[i,"color_name"]
    return cname

#function to get x,y coordinates of mouse double click
def draw_function(event, x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)

cv.namedWindow('image')
cv.setMouseCallback('image',draw_function)

while(1):

    cv.imshow("image",img)
    if (clicked):

        #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle
        cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)

        #Creating text string to display( Color name and RGB values )
        #text = getcolorname(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        text = getcolorname(r,g,b)
        #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        cv.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv.LINE_AA)

        #For very light colours we will display text in black colour
        if(r+g+b>=600):
            cv.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv.LINE_AA)

        clicked=False

    #Break the loop when user hits 'esc' key
    if cv.waitKey(20) & 0xFF ==27:
        break

cv.destroyAllWindows()
