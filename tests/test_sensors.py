# tests/test_sensors.py

import unittest
from sensor_monitor.sensors.ammonia_sensor import AmmoniaSensor
from sensor_monitor.sensors.ph_sensor import PHSensor
from sensor_monitor.sensors.o2_sensor import O2Sensor

class TestSensors(unittest.TestCase):
    def test_ammonia_sensor_safe(self):
        sensor = AmmoniaSensor()
        self.assertTrue(sensor.is_safe_level(0.5))
        self.assertFalse(sensor.is_safe_level(1.5))

    def test_ph_sensor_safe(self):
        sensor = PHSensor()
        self.assertTrue(sensor.is_safe_level(7.0))
        self.assertFalse(sensor.is_safe_level(9.0))

    def test_o2_sensor_safe(self):
        sensor = O2Sensor()
        self.assertTrue(sensor.is_safe_level(5.0))
        self.assertFalse(sensor.is_safe_level(3.0))

if __name__ == '__main__':
    unittest.main()