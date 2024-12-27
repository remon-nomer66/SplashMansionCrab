# sensors.py

import random

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

class AmmoniaSensor(BaseSensor):
    def __init__(self, interval=5):
        super().__init__("アンモニアセンサー", (0.0, 1.0), interval)

    def get_value(self):
        # ダミー値をランダムに生成
        return round(random.uniform(-0.5, 1.5), 2)

class PHSensor(BaseSensor):
    def __init__(self, interval=10):
        super().__init__("pHセンサー", (6.5, 8.5), interval)

    def get_value(self):
        # ダミー値をランダムに生成
        return round(random.uniform(6.0, 9.0), 2)

class O2Sensor(BaseSensor):
    def __init__(self, interval=7):
        super().__init__("酸素センサー", (4.0, 8.0), interval)

    def get_value(self):
        # ダミー値をランダムに生成
        return round(random.uniform(3.0, 9.0), 2)