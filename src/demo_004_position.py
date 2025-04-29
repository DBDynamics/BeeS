# 导入时间模块，用于处理时间相关操作
import time
# 从 DBDynamics 模块导入 BeeS 类
from DBDynamics import BeeS

# 创建 BeeS 类的实例，连接到指定串口设备
m = BeeS('/dev/ttyUSB0')
# 这里设置成当前要控制的设备 ID 号
mid = 0

# 高级使能设备，配置设备的限位和报警恢复策略
# 软件限位：无效-0，有效-1
# 传感器限位：生效-0，无效-1
# 报警：释放电机-0，自动恢复-1
m.setPowerOnPro(id=mid, limit_soft=0, limit_off=0, auto_recovery=0)

# 设置设备为平滑位置模式
m.setPositionMode(mid)

# 设置设备的最大运行速度为 2000
m.setTargetVelocity(mid, 2000)

# 设置设备的加减速时间为 500 毫秒
m.setAccTime(mid, 500)

# 循环 3 次
for loop in range(0, 3):
    # 设置设备的目标位置为 51200
    m.setTargetPosition(mid, 51200)
    # 等待设备到达目标位置
    m.waitTargetPositionReached(mid)

    # 设置设备的目标位置为 0
    m.setTargetPosition(mid, 0)
    # 等待设备到达目标位置
    m.waitTargetPositionReached(mid)

# 停止设备操作
m.stop()
