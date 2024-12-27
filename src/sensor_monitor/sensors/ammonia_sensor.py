# src/sensor_monitor/sensors/ammonia_sensor.py

import random
from sensor_monitor.sensors.base_sensor import BaseSensor

class AmmoniaSensor(BaseSensor):
    def __init__(self, interval=5):
        super().__init__("アンモニアセンサー", (0.0, 1.0), interval)

    def get_value(self):
        # ダミー値をランダムに生成
        return round(random.uniform(-0.5, 1.5), 2)