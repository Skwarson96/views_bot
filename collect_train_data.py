import pandas as pd
import requests

from stem import Signal
from stem.control import Controller
import time
import json
import threading
import logging
import timeit
import pandas as po

def get_tor_session():
    session = requests.session()
    session.proxies = {'http':  'socks5://127.0.0.1:9050',
                       'https': 'socks5://127.0.0.1:9050'}
    return session


def renew_connection():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password="123qwe")

        controller.signal(Signal.NEWNYM)


def thread_function(name, url, iter_1, iter_2):

    for i in range(iter_1):
        session = get_tor_session()

        ip_req = session.get("http://httpbin.org/ip").text

        ip_dict = json.loads(ip_req)
        new_ip = ip_dict['origin']

        for i2 in range(iter_2):
            req_ = session.get(url).text
            # print('thread nr:', name, 'iter:', i, '.', i2, new_ip)

        renew_connection()

        time.sleep(1)

def load_dataframe():

    data_df = pd.read_csv('dataset.csv')
    return data_df

def main():
    print("test main")
    dataset = load_dataframe()

    # HE HE HE HE :D
    url = 'https://camo.githubusercontent.com/f23e18ddb522dd44bfff1cee6226b6e381a23ce3f129b5b7e8877d3cd6ccdd2b/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d4a616b75622d4269656c6177736b69'

    threads_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    iter_1_list = [1, 2, 5, 10, 15, 20, 25, 40, 50]
    iter_2_list = [1, 2, 3, 4, 5]

    colect_data_iterations = 5


    counter = 1

    for threads_num in threads_num_list:
        for iter_1 in iter_1_list:
            for iter_2 in iter_2_list:
                for all_iter in range(colect_data_iterations):

                    start = timeit.default_timer()

                    threads = list()
                    for index in range(threads_num):
                        # print('start', index)
                        x = threading.Thread(target=thread_function, args=(index, url, iter_1, iter_2))
                        threads.append(x)
                        x.start()

                    for index, thread in enumerate(threads):
                        thread.join()
                        # print('finish', index)

                    stop = timeit.default_timer()

                    time_score = stop - start
                    time_score = int(time_score)
                    print('Stats:', 'all_iter', all_iter, 'threads_num', threads_num, 'iter_1', iter_1, 'iter_2', iter_2, 'time:', time_score)

                    dataset.loc[len(dataset.index)] = [threads_num, iter_1, iter_2, time_score]

                    counter = counter + 1
                    dataset.to_csv('dataset.csv', index=False)
                    # Stats: all_iter 4 threads_num 10 iter_1 50 iter_2 5 time: 0


if __name__ == '__main__':
    main()
