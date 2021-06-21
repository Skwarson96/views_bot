import requests

from stem import Signal
from stem.control import Controller
import time
import json


def get_tor_session():
    session = requests.session()

    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session

def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="123qwe")
        controller.signal(Signal.NEWNYM)

def main():
    print("test main")

    # HE HE HE HE :D
    url = 'https://camo.githubusercontent.com/f23e18ddb522dd44bfff1cee6226b6e381a23ce3f129b5b7e8877d3cd6ccdd2b/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d4a616b75622d4269656c6177736b69'


    for i in range(50):
        session = get_tor_session()

        ip_req = session.get("http://httpbin.org/ip").text

        ip_dict = json.loads(ip_req)
        new_ip = ip_dict['origin']

        for i2 in range(10):
            req_ = session.get(url).text
            print(i, '.', i2, new_ip)

        renew_connection()
        time.sleep(1)


if __name__ == '__main__':
    main()
