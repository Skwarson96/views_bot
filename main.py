import requests

from stem import Signal
from stem.control import Controller
import time
import json
import threading
import logging
import timeit
import argparse
from pathlib import Path
import pickle

from time_prediction import time_pred
from time_prediction import train_regressors


def get_tor_session():
    session = requests.session()
    session.proxies = {'http': 'socks5://127.0.0.1:9050',
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
            print('thread nr:', name, 'iter:', i, '.', i2, new_ip)

        renew_connection()

        time.sleep(1)


def main():
    print("test main")


    parser = argparse.ArgumentParser()
    parser.add_argument('threads_num', type=int)
    parser.add_argument('iter_1', type=int)
    parser.add_argument('iter_2', type=int)
    args = parser.parse_args()

    # HE HE HE HE :D

    url = 'https://camo.githubusercontent.com/f23e18ddb522dd44bfff1cee6226b6e381a23ce3f129b5b7e8877d3cd6ccdd2b/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d4a616b75622d4269656c6177736b69'

    threads_num = args.threads_num
    iter_1 = args.iter_1
    iter_2 = args.iter_2


    # time_prediction, time_prediction_clear = time_pred(threads_num, iter_1, iter_2)



    train_regressors(threads_num, iter_1, iter_2)

    with Path('regressors/reg_RF.p').open('rb') as classifier_file:
        reg_RF = pickle.load(classifier_file)

    with Path('regressors/reg_SVR.p').open('rb') as classifier_file:
        reg_SVR = pickle.load(classifier_file)

    time_prediction_rf = reg_RF.predict([[threads_num, iter_1, iter_2]])
    time_prediction_svr = reg_SVR.predict([[threads_num, iter_1, iter_2]])
    # time_prediction_clear = reg_RF.predict([[threads_num, iter_1, iter_2]])


    print("Your variables: threads:", threads_num, ", iter_1:", iter_1, ", iter_2:", iter_2)
    print("Time predicted Random Forest:", time_prediction_rf)
    print("Time predicted SVR:", time_prediction_svr)
    # print("Time predicted on clear dataset:", time_prediction_clear)

    start = timeit.default_timer()

    threads = list()
    for index in range(threads_num):
        # logging.info("Main    : create and start thread %d.", index)
        # print('start', index)
        x = threading.Thread(target=thread_function, args=(index, url, iter_1, iter_2))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
        # print('finish', index)

    stop = timeit.default_timer()

    print('Time of:', threads_num * iter_1 * iter_2, 'requests:', stop - start)
    print("Time prediction error Random Forest:", abs((stop - start) - time_prediction_rf))
    print("Time prediction error SVR:", abs((stop - start) - time_prediction_svr))

    # print("Time prediction error wth clear dataset:", abs((stop - start) - time_prediction_clear))



if __name__ == '__main__':
    main()
