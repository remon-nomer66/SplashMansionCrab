# src/sensor_monitor/alerts/alert.py

import logging

class Alarm:
    def __init__(self, strings):
        """
        Alarm Class
        :param strings: Strings instance
        """
        self.strings = strings

    def trigger(self):
        """
        Trigger the alarm
        """
        # Get log message from Strings
        logging.warning(self.strings.get('ALARM_TRIGGER'))
        # Implement actual alarm triggering logic here
        pass