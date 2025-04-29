# 导入时间模块，用于处理时间相关操作
import time
# 从 DBDynamics 模块导入 BeeS 类
from DBDynamics import BeeS

# 创建 BeeS 类的实例，连接到指定串口设备
m = BeeS('/dev/ttyUSB0')
# 定义设备 ID，设置为 0
mid = 0
# 默认失能设备，失能后释放电机
m.setPowerOff(mid)

# 停止设备操作
m.stop()
