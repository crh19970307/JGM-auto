import os
import time

# 1920x1080的结果，否则使用preprocess.py得到的结果
x=[299, 555, 802, 289, 555, 815, 295, 547, 802, 647, 810, 964]
y=[743, 616, 495, 1004, 872, 755, 1254, 1129, 1006, 1609, 1550, 1473]

while 1:
#     for i in range(8):
#         os.popen("adb shell  input swipe %d %d %d %d"%(x[i],y[i],x[i+1],y[i+1]))
#         time.sleep(0.3)
#     time.sleep(3)
    for i in range(9,12):
        for j in range(9):
            os.popen("adb shell  input swipe %d %d %d %d"%(x[i],y[i],x[j],y[j]))
            time.sleep(0.5)
