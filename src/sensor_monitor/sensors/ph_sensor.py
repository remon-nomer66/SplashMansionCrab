# src/sensor_monitor/sensors/ph_sensor.py

import random
from sensor_monitor.sensors.base_sensor import BaseSensor

class PHSensor(BaseSensor):
    def __init__(self, name, interval=5):
        super().__init__(name, (6.5, 8.5), interval)

    def get_value(self):
        # Generate dummy value
        return round(random.uniform(6.0, 9.0), 2)