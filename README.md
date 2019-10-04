# JGM-auto
家国梦辅助脚本

# 环境

* windows
* adb
* 雷电模拟器
* python3

# 基准点校正

如果使用其他模拟器以及分辨率，可能需要对12个点进行校正，否则无需校正，直接运行即可。

```bash
adb shell getevent -p | findstr 003[56]
```

得到Wp与Hp，填入preprocess.py

```bash
adb shell getevent | findstr 003[56]
```

再从左到右、从上到下依次点击12个点，将结果放入preprocess.py

```bash
python preprocess.py
```

得到x坐标列表与y坐标列表，填入run.py

# 运行

如果使用的雷电模拟器1920x1080（或者其他1920x1080的设备），直接运行即可

```bash
python run.py
```

------

如果有问题，直接新建issue即可。

