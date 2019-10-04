import os
import time
W = 1080
H = 1920
x=[]
y=[]

# 由 adb shell getevent -p | findstr 003[56] 得到
Wp = 19199
Hp = 10799

# 由 adb shell getevent | findstr 003[56] 得到
getcord = "/dev/input/event5: 0003 0035 000014c9\n/dev/input/event5: 0003 0036 00001057\n/dev/input/event5: 0003 0035 00002697\n/dev/input/event5: 0003 0036 00000d8c\n/dev/input/event5: 0003 0035 000037b5\n/dev/input/event5: 0003 0036 00000ae2\n/dev/input/event5: 0003 0035 0000141c\n/dev/input/event5: 0003 0036 00001610\n/dev/input/event5: 0003 0035 00002697\n/dev/input/event5: 0003 0036 0000132e\n/dev/input/event5: 0003 0035 000038a9\n/dev/input/event5: 0003 0036 0000109a\n/dev/input/event5: 0003 0035 00001484\n/dev/input/event5: 0003 0036 00001b91\n/dev/input/event5: 0003 0035 0000260b\n/dev/input/event5: 0003 0036 000018d0\n/dev/input/event5: 0003 0035 000037b5\n/dev/input/event5: 0003 0036 0000161b\n/dev/input/event5: 0003 0035 00002cf9\n/dev/input/event5: 0003 0036 0000235a\n/dev/input/event5: 0003 0035 00003840\n/dev/input/event5: 0003 0036 0000220f\n/dev/input/event5: 0003 0035 000042fc\n/dev/input/event5: 0003 0036 00002062"

for id,item  in enumerate(getcord.split('\n')):
    cord = item.split()[-1]
    if(id%2 == 0):
        x.append(int(int(cord,16)*W/Wp))
    else:
        y.append(int(int(cord,16)*H/Hp))
print(x)
print(y)
