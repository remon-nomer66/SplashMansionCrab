# src/sensor_monitor/notifications/send_sms.py

import logging

class SMSNotification:
    def __init__(self, strings, recipients=None):
        """
        SMS Notification Class
        :param strings: Strings instance
        :param recipients: List of recipients
        """
        self.strings = strings
        self.recipients = recipients if recipients else []

    def set_recipients(self, recipients):
        """
        Set the list of recipients
        """
        self.recipients = recipients

    def send_notification(self, message, safe_min, safe_max):
        """
        Send SMS notification
        :param message: Dictionary containing 'sensor_name' and 'value'
        :param safe_min: Minimum safe value
        :param safe_max: Maximum safe value
        """
        formatted_message = self.strings.get(
            'SENSOR_DANGER_MESSAGE',
            sensor_name=message['sensor_name'],
            value=message['value'],
            min=safe_min,
            max=safe_max
        )
        for recipient in self.recipients:
            # Implement actual SMS sending logic here
            # Example: response = sms_api.send(to=recipient, message=formatted_message)
            logging.info(self.strings.get('SMS_SENT', message=formatted_message))
            # Dummy send as log
            pass