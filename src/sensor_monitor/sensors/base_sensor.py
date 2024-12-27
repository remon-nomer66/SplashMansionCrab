# src/sensor_monitor/sensors/base_sensor.py

class BaseSensor:
    def __init__(self, name, safe_range, interval):
        """
        基本センサークラス
        :param name: センサー名
        :param safe_range: 安全範囲 (タプル: (最小値, 最大値))
        :param interval: 値を取得する間隔（秒）
        """
        self.name = name
        self.safe_range = safe_range
        self.interval = interval

    def get_value(self):
        """
        センサー値を取得する（サブクラスで実装）
        """
        raise NotImplementedError

    def is_safe_level(self, value):
        """
        値が安全範囲内かをチェックする
        """
        return self.safe_range[0] <= value <= self.safe_range[1]