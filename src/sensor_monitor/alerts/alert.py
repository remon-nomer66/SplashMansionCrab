# src/sensor_monitor/alerts/alert.py

import logging

class Alarm:
    def __init__(self):
        pass

    def trigger(self):
        """
        アラームを鳴らす処理
        """
        # 実際のアラーム鳴動処理をここに記述
        logging.warning("アラームを鳴らします。")
        # 例: GPIOピンを操作してアラームを鳴らすなど
        pass