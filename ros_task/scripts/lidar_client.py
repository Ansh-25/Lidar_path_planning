#!/usr/bin/env python
from __future__ import print_function

import sys
import rospy
from ros_task.srv import *

import PIL
from PIL import Image
import pathlib
import math
import random

print("client started")

def lidar_client(x,y):
    rospy.wait_for_service('lidar_scan')
    try:
        lidar_scan = rospy.ServiceProxy('lidar_scan',lidarScan)
        resp1 = lidar_scan(x,y)
        return_array = []
        return resp1.lidar_array

    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

def usage():
    return "%s [x y]" %sys.argv[0]

im = PIL.Image.new(mode = "RGB", size = (400, 400))

centerX = 350
centerY = 350
im.putpixel((int(centerX),int(centerY)), (255,255,255))

for j in range(1,100,1):
    if (im.getpixel((centerX, centerY)) == 0):
        centerX = random.randint(1,399)
        centerY = random.randint(1,399)
        j = j-1
        continue
    elif(im.getpixel((centerX, centerY)) == (255,255,255)):
        return_array = lidar_client(centerX,centerY)

        for i in range(0,360,1):
            r = 0

            for r in range(0,return_array[2*i + 1]+1):
                currentX = round(centerX + r*math.cos(i*math.pi/180))
                currentY = round(centerY + r*math.sin(i*math.pi/180))
                if (currentX == 399 or currentY == 399 or currentX == 1 or currentY ==1):
                    break
                elif ((currentX < 400) and (currentY < 400) ):
                    im.putpixel((int(currentX),int(currentY)), (255,255,255))

    print(j)
    centerX = random.randint(1,399)
    centerY = random.randint(1,399)

im.show()
im.save('botmap1.jpg')