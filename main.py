import os
import logging
import serial
from picloud_client import HttpClient


SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_RATE = 9600
PICLOUD_EVENT = 'home:thpl'

PICLOUD_HTTP_URL = os.getenv('PICLOUD_HTTP_URL')
assert PICLOUD_HTTP_URL

PICLOUD_API_KEY = os.getenv('PICLOUD_API_KEY')
assert PICLOUD_API_KEY


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/tmp/thpl-data-reporter.log',
    filemode='w')


def main():
    picloud = HttpClient(
        url=PICLOUD_HTTP_URL,
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
