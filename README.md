## What does this repo contains
This code setups a basic sever client model in ROS(Robot Operating System).  
The task is to generate back environment images from the LIDAR sensor data.
  
- lidar_generated_images contains the regenrated path using the model
- server.py and client.py contain the main logic for the LIDAR sensor data extraction and conversion
- client receives a 32bit integer array as LIDAR data and further converts this to a map.

## How Does LIDAR Work? 
A typical LIDAR sensor emits pulsed light waves into the surrounding environment. These pulses bounce off surrounding objects and return to the sensor. The sensor uses the time it took for each pulse to return to the sensor to calculate the distance it traveled.
