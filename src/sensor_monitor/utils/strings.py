# src/sensor_monitor/utils/strings.py

class Strings:
    def __init__(self, language='ja'):
        self.language = language
        self.translations = {
            'ja': {
                'SENSOR_VALUE': "{sensor_name}の値: {value}",
                'SENSOR_DANGER': "{sensor_name}の値({value})が危険範囲を超えています。",
                'SENSOR_SAFE': "{sensor_name}の値({value})は安全範囲内です。",
                'ALARM_TRIGGER': "アラームを鳴らします。",
                'SMS_SENT': "SMS送信: {message}",
                'ERROR_FETCHING_VALUE': "{sensor_name}の値の取得中にエラーが発生: {error}",
                'PROGRAM_EXIT': "プログラムを終了します。"
            },
            'en': {
                'SENSOR_VALUE': "Value of {sensor_name}: {value}",
                'SENSOR_DANGER': "Value of {sensor_name} ({value}) exceeds the danger range.",
                'SENSOR_SAFE': "Value of {sensor_name} ({value}) is within the safe range.",
                'ALARM_TRIGGER': "Triggering alarm.",
                'SMS_SENT': "SMS Sent: {message}",
                'ERROR_FETCHING_VALUE': "Error fetching value from {sensor_name}: {error}",
                'PROGRAM_EXIT': "Exiting program."
            }
            # 必要に応じて他の言語を追加
        }

    def get(self, key, **kwargs):
        message = self.translations.get(self.language, {}).get(key, "")
        return message.format(**kwargs)