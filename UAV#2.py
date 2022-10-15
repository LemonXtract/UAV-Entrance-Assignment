import math
from math import pi

#Takes in user input for the values needed
X, Y, L, H, V = [float(x) for x in input("Enter multiple value: ").split()]
  
#Uses the fov and trig to determine pitch
distanceToCenter = (X/2)/(math.tan((V*pi/180)/2))
pitchRadians = math.atan((0-Y/2)/distanceToCenter)
pitch = pitchRadians * 180 / pi
 
#Uses the fov and trig to determine yaw
distanceToCenter = (X/2)/(math.tan((H*pi/180)/2))
yawRadians = math.atan((0-Y/2)/distanceToCenter)
yaw = yawRadians * 180 / pi  
 
 
#prints results
print(round(yaw), round(-pitch))

#20.8 15.7 50 10.5 -42.6
