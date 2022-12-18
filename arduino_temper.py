import serial
import time
import requests


def flask_post(API_key, mac_address, field, data):
    if not isinstance(data, str):
        data = str(data)
    if not isinstance(field, str):
        field = str(field)
    base_url = 'http://127.0.0.1:5000/update'
    api_key_url = '/API_key=' + API_key
    mac_url = '/mac=' + mac_address
    field_url = '/field=' + field
    data_url = '/data=' + str(data)
    url = base_url + api_key_url + mac_url + field_url + data_url
    print(url)
    response = requests.get(url)
    print(response.text)


# connect to serial port and read data
def read_temperature():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1, stopbits=1)
    time.sleep(2)

    for i in range(2):
        line = ser.readline()  # read a byte string
        string = line.decode()  # convert the byte string to a unicode
        stripped_string = string.strip()
        if stripped_string == '\x00':
            stripped_string = '0'
            print('was 00')
        num = int(stripped_string)
        print(num)

    ser.close()
    return num


while True:
    print('while begin')
    try:
        flask_post('GTW89NF3', '6c:rf:7f:2b:0e:g8', 1, read_temperature())
    except:
        pass
    time.sleep(60)
    print('while end')


