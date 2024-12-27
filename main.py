# main.py

import asyncio
import yaml
import logging
from logging.handlers import RotatingFileHandler
from sensors import AmmoniaSensor, PHSensor, O2Sensor
from alert import Alarm
from send_sms import SMSNotification
from strings import Strings

# ロギングの設定
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # ローテーティングファイルハンドラー
    handler = RotatingFileHandler("sensor_monitor.log", maxBytes=5*1024*1024, backupCount=5, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # ストリームハンドラー（コンソール出力）
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# 設定ファイルをロードする関数
def load_config(config_path='config.yaml'):
    with open(config_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

async def monitor_sensor(sensor, alarm, sms_notifier, strings):
    """
    個別のセンサーを監視する非同期関数
    """
    while True:
        try:
            value = sensor.get_value()
            logging.info(strings.get('SENSOR_VALUE', sensor_name=sensor.name, value=value))
            
            if not sensor.is_safe_level(value):
                logging.warning(strings.get('SENSOR_DANGER', sensor_name=sensor.name, value=value))
                alarm.trigger()
                message = (
                    f"{sensor.name}の値が危険: {value}。\n"
                    f"安全範囲: {sensor.safe_range[0]} ～ {sensor.safe_range[1]}"
                )
                sms_notifier.send_notification(message)
            else:
                logging.info(strings.get('SENSOR_SAFE', sensor_name=sensor.name, value=value))

        except Exception as e:
            logging.error(strings.get('ERROR_FETCHING_VALUE', sensor_name=sensor.name, error=e))
        
        await asyncio.sleep(sensor.interval)

async def main():
    # ロギングの設定
    setup_logging()

    # 設定ファイルのロード
    config = load_config()

    # 使用言語の設定
    language = config.get('language', 'ja')
    strings = Strings(language=language)

    # グローバルなセンサー取得頻度の設定
    global_interval = config.get('sensor_interval', 5)  # デフォルトは5秒

    # センサーの初期化（コード内で直接定義）
    sensors = [
        AmmoniaSensor(interval=global_interval),
        PHSensor(interval=global_interval),
        O2Sensor(interval=global_interval)
    ]

    # アラームの初期化
    alarm = Alarm()

    # SMS通知の初期化
    sms_notifier = SMSNotification()
    if config.get('sms', {}).get('enabled', False):
        recipients = config['sms'].get('recipients', [])
        sms_notifier.set_recipients(recipients)

    # 監視タスクの作成
    tasks = []
    for sensor in sensors:
        task = asyncio.create_task(monitor_sensor(sensor, alarm, sms_notifier, strings))
        tasks.append(task)

    # タスクの実行
    try:
        await asyncio.gather(*tasks)
    except asyncio.CancelledError:
        logging.info(strings.get('PROGRAM_EXIT'))
    except KeyboardInterrupt:
        logging.info(strings.get('PROGRAM_EXIT'))

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("プログラムを終了します。")