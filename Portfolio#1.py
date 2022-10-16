import math
from math import pi

with open("values.txt", "r") as f:
    f_contents = f.read()
    imgDimX, imgDimY, centerX, centerY, focalLength, sensorHeight, objRealHeight, objImgHeight, hfov, vfov = f_contents

#Takes in user input for the values needed
#imgDimX, imgDimY, centerX, centerY, focalLength, sensorHeight, objRealHeight, objImgHeight, hfov, vfov = x = [float(x) for x in input("Enter multiple value: ").split()]
 
#Calculates distance to object in meters
distance = (focalLength * objRealHeight * imgDimY)/(objImgHeight * sensorHeight)/1000
 
#Uses the fov and trig to determine pitch
distanceToCenter = (imgDimY/2)/(math.tan((vfov*pi/180)/2))
pitchRadians = math.atan((centerY-imgDimY/2)/distanceToCenter)
pitch = pitchRadians * 180 / pi
 
#Uses the fov and trig to determine yaw
distanceToCenter = (imgDimX/2)/(math.tan((hfov*pi/180)/2))
yawRadians = math.atan((centerX-imgDimX/2)/distanceToCenter)
yaw = yawRadians * 180 / pi  
 
#Finds x and y offset through trig
xOffSet = distance * math.sin(yawRadians)
yOffSet = distance * math.sin(pitchRadians)
 
#prints results
print(round(yaw), round(-pitch), round(distance), round(xOffSet), round(yOffSet))

#512 341 300 150 8 8.8 1524 80 77.3 62
