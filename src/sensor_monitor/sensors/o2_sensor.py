# src/sensor_monitor/sensors/o2_sensor.py

import random
from sensor_monitor.sensors.base_sensor import BaseSensor

class O2Sensor(BaseSensor):
    def __init__(self, name, interval=5):
        super().__init__(name, (4.0, 8.0), interval)

    def get_value(self):
        # Generate dummy value
        return round(random.uniform(3.0, 9.0), 2)