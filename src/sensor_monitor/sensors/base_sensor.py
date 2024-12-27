# src/sensor_monitor/sensors/base_sensor.py

class BaseSensor:
    def __init__(self, name, safe_range, interval):
        """
        Base Sensor Class
        :param name: Sensor name
        :param safe_range: Safe range (tuple: (min, max))
        :param interval: Interval to fetch value (seconds)
        """
        self.name = name
        self.safe_range = safe_range
        self.interval = interval

    def get_value(self):
        """
        Fetch sensor value (to be implemented by subclasses)
        """
        raise NotImplementedError

    def is_safe_level(self, value):
        """
        Check if the value is within the safe range
        """
        return self.safe_range[0] <= value <= self.safe_range[1]