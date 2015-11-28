import logging
import serial
from picloud_client import PiCloud


SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_RATE = 9600
PICLOUD_EVENT = 'home:thpl'


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='/tmp/thpl-data-reporter.log',
    filemode='w')


def main():
    picloud = PiCloud(client_name='THPL-Data-Reporter')
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
