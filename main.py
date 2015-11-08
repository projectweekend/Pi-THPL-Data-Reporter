import serial
from picloud_client import PiCloud


SERIAL_PORT = '/dev/ttyAMA0'
SERIAL_RATE = 9600
PICLOUD_EVENT = 'home:thpl'


def main():
    picloud = PiCloud()
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        sensor_json = ser.readline()
        picloud.publish(event=PICLOUD_EVENT, data=sensor_json)


if __name__ == "__main__":
    main()
