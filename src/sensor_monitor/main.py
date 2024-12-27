# src/sensor_monitor/main.py

import sys
import os

# Get the current file's directory
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the 'src' directory path
src_dir = os.path.dirname(current_dir)
# Add 'src' directory to sys.path
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

import asyncio
import yaml
import logging
from logging.handlers import RotatingFileHandler
from sensor_monitor.sensors.ammonia_sensor import AmmoniaSensor
from sensor_monitor.sensors.ph_sensor import PHSensor
from sensor_monitor.sensors.o2_sensor import O2Sensor
from sensor_monitor.alerts.alert import Alarm
from sensor_monitor.notifications.send_sms import SMSNotification
from sensor_monitor.utils.strings import Strings

# Setup logging
def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Rotating file handler
    handler = RotatingFileHandler("sensor_monitor.log", maxBytes=5*1024*1024, backupCount=5, encoding='utf-8')
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Stream handler (console output)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)

# Load configuration from file
def load_config(config_path='config.yaml'):
    config_file = os.path.join(current_dir, config_path)
    print(f"Loading config from: {config_file}")  # Debug
    if not os.path.exists(config_file):
        logging.error(f"Configuration file not found: {config_file}")
        sys.exit(1)
    try:
        with open(config_file, 'r', encoding='utf-8') as file:
            config = yaml.safe_load(file)
            print(f"Config loaded: {config}")  # Debug
            return config
    except yaml.YAMLError as e:
        logging.error(f"Error parsing configuration file: {e}")
        sys.exit(1)

async def monitor_sensor(sensor, alarm, sms_notifier, strings):
    """
    Asynchronously monitor a single sensor
    """
    while True:
        try:
            value = sensor.get_value()
            logging.info(strings.get('SENSOR_VALUE', sensor_name=sensor.name, value=value))
            
            if not sensor.is_safe_level(value):
                logging.warning(strings.get('SENSOR_DANGER', sensor_name=sensor.name, value=value))
                alarm.trigger()
                message = {
                    'sensor_name': sensor.name,
                    'value': value
                }
                sms_notifier.send_notification(message, sensor.safe_range[0], sensor.safe_range[1])
            else:
                logging.info(strings.get('SENSOR_SAFE', sensor_name=sensor.name, value=value))

        except Exception as e:
            logging.error(strings.get('ERROR_FETCHING_VALUE', sensor_name=sensor.name, error=e))
        
        await asyncio.sleep(sensor.interval)

async def main():
    # Setup logging
    setup_logging()

    # Load configuration
    config = load_config()

    # Set language
    language = config.get('language', 'ja')
    print(f"Language set to: {language}")  # Debug
    strings = Strings(language=language)
    print(f"Strings language: {strings.language}")  # Debug

    # Global sensor interval
    global_interval = config.get('sensor_interval', 5)  # Default 5 seconds

    # Initialize sensors with names from Strings
    sensors = [
        AmmoniaSensor(name=strings.get('SENSOR_NAME_AMMONIA'), interval=global_interval),
        PHSensor(name=strings.get('SENSOR_NAME_PH'), interval=global_interval),
        O2Sensor(name=strings.get('SENSOR_NAME_O2'), interval=global_interval)
    ]

    # Initialize Alarm with Strings
    alarm = Alarm(strings)

    # Initialize SMSNotification with Strings
    sms_notifier = SMSNotification(strings)
    if config.get('sms', {}).get('enabled', False):
        recipients = config['sms'].get('recipients', [])
        sms_notifier.set_recipients(recipients)

    # Create monitoring tasks
    tasks = []
    for sensor in sensors:
        task = asyncio.create_task(monitor_sensor(sensor, alarm, sms_notifier, strings))
        tasks.append(task)

    # Run tasks
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
        # Log program exit message
        config = load_config()
        language = config.get('language', 'ja')
        strings = Strings(language=language)
        print(f"Language set to: {language}")  # Debug
        print(f"Strings language: {strings.language}")  # Debug
        logging.info(strings.get('PROGRAM_EXIT'))