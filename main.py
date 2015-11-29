import os
import logging
import serial
from picloud_client import PubClient


SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_RATE = 9600
PICLOUD_EVENT = 'home:thpl'

PICLOUD_PUB_URL = os.getenv('PICLOUD_PUB_URL')
assert PICLOUD_PUB_URL

PICLOUD_API_KEY = os.getenv('PICLOUD_API_KEY')
assert PICLOUD_API_KEY


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/tmp/thpl-data-reporter.log',
    filemode='w')


def main():
    picloud = PubClient(
        url=PICLOUD_PUB_URL,
        api_key=PICLOUD_API_KEY,
        client_name='THPL-Data-Reporter')
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        try:
            sensor_json = ser.readline()
            picloud.publish(event=PICLOUD_EVENT, data=sensor_json)
        except Exception as e:
            logging.exception(e)
            raise e


if __name__ == "__main__":
    main()
