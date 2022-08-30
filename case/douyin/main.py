import subprocess


# 1.开启服务
subprocess.getoutput("adb kill-server")
subprocess.getoutput("adb start-server")

# 2.连接模拟器
subprocess.getoutput("adb connect 127.0.0.1:7555")

# 3.发送指令
while True:
    subprocess.getoutput("adb -s 127.0.0.1:7555 shell input tap 1145 1368")
    subprocess.getoutput("adb -s 127.0.0.1:7555 shell input swipe 242 1600 941 457 800")

