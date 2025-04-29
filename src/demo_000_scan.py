# 从 DBDynamics 模块导入 BeeS 类
from DBDynamics import BeeS
# 注释：在 Windows 系统下，可使用 'com3' 端口初始化对象，当前使用 Linux 系统的串口
# for windows, m = Bee('com3')
# 初始化 BeeS 类的实例，使用 Linux 系统的串口 '/dev/ttyUSB0'
m = BeeS('/dev/ttyUSB0')
# 调用实例的 scanDevices 方法，扫描设备
m.scanDevices()
# 调用实例的 stop 方法，停止操作并释放资源
m.stop()
