from cmath import pi
import cv2 as cv
import math
import numpy as np

#Takes in the image and converts it to a hsv color scheme
img = cv.imread("Images/pathmarker_3.png")
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

#Sets the upper and lower range for masking
lower_range = np.array([0, 120, 10])
upper_range = np.array([20, 225, 225])

#Masks the image with upper and lower ranges of the marker color
mask = cv.inRange(hsv, lower_range, upper_range)
res_yellow = cv.bitwise_and(hsv, hsv, mask = mask)

#Looks for contours in the masked image, creating a rectangle around it if it's bigger than 500
contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
if len(contours) != 0:  
    for contour in contours:
        if cv.contourArea(contour) > 500:
            x, y, w, h = cv.boundingRect(contour)
            #cv.rectangle(res_yellow, (x, y), (x + w, y + h), (0, 0, 255), 3)
            rect = cv.minAreaRect(contour)
            box = cv.boxPoints(rect)
            box = np.int0(box) 
            width = int(rect[1][0])
            height = int(rect[1][1])

#Calculates the angle using the boundingRect corners
hypotenuse = math.sqrt(w*w + h*h)
radians = math.asin(w/hypotenuse)
angle = radians*180/pi

#Uses minAreaRect values to determine which direction the marker is point
#Not using minAreaRect values for angles because less accurate
if width > height:
    angle = -angle

#prints out the rounded results
print(math.floor(x + w/2), math.floor(y + h/2), round(angle))

#cv.imshow("HSV", hsv)
#cv.imshow("Mask", res_yellow)
#cv.waitKey(0)
#cv.destroyAllWindows()

#https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#https://www.youtube.com/watch?v=cMJwqxskyek
#https://imagecolorpicker.com/en
#https://www.rapidtables.com/convert/color/rgb-to-hsv.html
#https://automaticaddison.com/how-to-determine-the-orientation-of-an-object-using-opencv/
#https://docs.opencv.org/3.4/dd/d49/tutorial_py_contour_features.html
#https://www.codegrepper.com/code-examples/python/image+frame+size+opencv