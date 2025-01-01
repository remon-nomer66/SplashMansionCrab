# src/sensor_monitor/sensors/ammonia_sensor.py

import random
from sensor_monitor.sensors.base_sensor import BaseSensor

class AmmoniaSensor(BaseSensor):
    def __init__(self, name, interval=5):
        super().__init__(name, (0.0,0.2), interval)

    def check_amo_list(amo_list):
        if len(amo_list) >= 5 and all(value > 1 for value in amo_list[-5:]):
            return 1
        return 0

    
    def get_value(self):
        # Generate dummy value

        # RS485からデータを取得するコードをここに追加します
        # return で取得したデータを返します
        return round(random.uniform(-0.5, 1.5), 2)