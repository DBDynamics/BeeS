# 导入时间模块，用于处理时间相关操作
import time
# 从 DBDynamics 模块导入 BeeS 类
from DBDynamics import BeeS

# 创建 BeeS 类的实例，连接到指定串口设备
m = BeeS('/dev/ttyUSB0')
# 定义设备 ID，设置为 0
mid = 0
# 默认使能设备，软件限位无效，传感器限位生效，报警时释放电机
m.setPowerOn(mid)

# 高级使能设备，配置设备的限位和报警恢复策略
# 软件限位：无效-0，有效-1
# 传感器限位：生效-0，无效-1
# 报警：释放电机-0，自动恢复-1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)

# 停止设备操作
m.stop()
