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

    # このメソッドは、センサーの値が安全範囲内にあるかどうかを確認します。
    # 出力は、センサーの値が安全範囲内にある場合はTrue、それ以外の場合はFalseです。
    def is_safe_level(self, value):
        """
        Check if the value is within the safe range
        """
        # 各値をリストに保存しておく。
        # リストに追加していく
        # 喫緊の10この値が、安全範囲を超えているかどうかを確認する
        # 超えていたら、警告を出す False    
        # 超えていなかったら、安全であると表示する  True

        # returnでは、センサーの値が安全範囲内にあるかどうかを確認します。
        # 返す値は、センサーの値が安全範囲内にある場合はTrue、それ以外の場合はFalseです。
        return self.safe_range[0] <= value <= self.safe_range[1]