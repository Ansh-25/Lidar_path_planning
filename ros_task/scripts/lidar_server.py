#!/usr/bin/env python
from __future__ import print_function

from ros_task.srv import lidarScan,lidarScanResponse
import rospy

import PIL
from PIL import Image
import pathlib
import math

def lidar_scan(centerX,centerY):
    map_name = 'map1.jpg'
    image = Image.open(pathlib.Path(map_name))
    image = image.convert('1')
    return_array = []
    no_of_rays = 360

    image.thumbnail((400, 400))

    image_size = min(image.size)

    if image.getpixel((centerX, centerY)) == 0:
        print('invalid')
    else:
        for i in range(0,360,int(360/no_of_rays)):
            r = 0

            currentX = round(centerX + r*math.cos(i*math.pi/180))
            currentY = round(centerY + r*math.sin(i*math.pi/180))

            while ((currentX < image_size and currentX >= 0) and (currentY < image_size and currentY >=0) and (image.getpixel((currentX, currentY)) != 0)):
                currentX = round(centerX + r*math.cos(i*math.pi/180))
                currentY = round(centerY + r*math.sin(i*math.pi/180))
                r+=1

            return_array.append(i)
            return_array.append(r)
    return return_array

def handle_lidar_scan(req):
    lidar_array = lidar_scan(req.centerX,req.centerY)
    return lidarScanResponse(lidar_array)

def lidar_server():
    rospy.init_node('lidar_server')
    s = rospy.Service('lidar_scan',lidarScan,handle_lidar_scan)
    print("Ready to scan")
    rospy.spin()

if __name__ == "__main__":
    lidar_server()
