import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def show_plot(index, real_vals, rf_vals, svr_vals, dtr_vals, lr_vals):

    # plt.figure()
    # plt.plot(index, real_vals)
    # plt.plot(index, rf_vals)
    # plt.plot(index, svr_vals)
    # plt.plot(index, dtr_vals)
    # plt.plot(index, lr_vals)
    # plt.legend(['Real vals', 'RF vals', 'SVR vals', 'DTR vals', 'LR vals'])

    plt.figure()
    plt.plot(index, real_vals)
    plt.plot(index, dtr_vals)
    plt.legend(['Real vals', 'DTR vals'])
    plt.xlabel('Index')
    plt.ylabel('Time')
    plt.show()

    # plt.figure()
    # plt.plot(index, real_vals)
    # plt.plot(index, rf_vals)
    # plt.legend(['Real vals', 'RF vals'])
    # plt.xlabel('Index')
    # plt.ylabel('Time [s]')
    # plt.show()


def req_num_check(dataframe):

    threads = dataframe['threads'].unique()

    error_dict = {}
    error_dict['forecast_error'] = []
    error_dict['mean_forecast_error'] = []
    error_dict['mae'] = []
    error_dict['mse'] = []
    error_dict['rmse'] = []

    for thread_ in threads:
        # skip 0
        if thread_ == 0:
            continue

        thread_data = dataframe.loc[dataframe['threads'] == thread_]
        forecast_error = thread_data['real_req_num'].sum() - thread_data['exp_req_num'].sum()
        mean_forecast_error = np.mean(thread_data['real_req_num'] - thread_data['exp_req_num'])
        mae = mean_absolute_error(thread_data['real_req_num'], thread_data['exp_req_num'])
        mse = mean_squared_error(thread_data['real_req_num'], thread_data['exp_req_num'])
        rmse = np.sqrt(mse)

        error_dict['forecast_error'].append(forecast_error)
        error_dict['mean_forecast_error'].append(mean_forecast_error)
        error_dict['mae'].append(mae)
        error_dict['mse'].append(mse)
        error_dict['rmse'].append(rmse)


    print(error_dict)

    ax1 = plt.subplot(511)
    ax1.plot(threads[1:], error_dict['forecast_error'])
    ax1.set_title("Forecast Error")

    ax2 = plt.subplot(512)
    ax2.plot(threads[1:], error_dict['mean_forecast_error'])
    ax2.set_title("Mean Forecast Error")

    ax3 = plt.subplot(513)
    ax3.plot(threads[1:], error_dict['mae'])
    ax3.set_title("Mean Absolute Error")

    ax4 = plt.subplot(514)
    ax4.plot(threads[1:], error_dict['mse'])
    ax4.set_title("Mean Squared Error")

    ax5 = plt.subplot(515)
    ax5.plot(threads[1:], error_dict['rmse'])
    ax5.set_title("Root Mean Squared Error")

    plt.show()


    # plt.plot(threads[1:], error_dict['mae'])
    # plt.title("Mean Absolute Error")
    # plt.xlabel('Threads number')
    # plt.ylabel('MAE (requests number)')
    # # plt.plot(index, exp_num)
    # # plt.legend(['Real num', 'Exp num'])
    # plt.show()



def time_to_req_num(dataframe):

    real_time = dataframe['real_time']
    real_num_of_req = dataframe['real_req_num']

    ratio = real_num_of_req/real_time

    max_idx = ratio.idxmax()
    print(dataframe.iloc[max_idx, :])

    dataframe = dataframe.sort_values(by=['threads'])
    dataframe.reset_index(drop=True, inplace=True)

    # plt.plot(dataframe.index, ratio)
    plt.scatter(dataframe['threads'], ratio)
    plt.title("Ratio of the number of requests to time by threads ")
    plt.xlabel('Thread')
    plt.ylabel('real_num_of_req/real_time')
    plt.show()


def main():

    # open test dataset
    df = pd.read_csv('datasets/test_dataset.csv')

    df['exp_req_num'] = df['threads'] * df['iter_1'] * df['iter_2']

    realVals = df['real_time']

    rf_forecast_error = realVals.sum() - df['rf_time'].sum()
    svr_forecast_error = realVals.sum() - df['svr_time'].sum()
    dtr_forecast_error = realVals.sum() - df['dtr_time'].sum()
    lr_forecast_error = realVals.sum() - df['lr_time'].sum()

    rf_mean_forecast_error = np.mean(realVals - df['rf_time'])
    svr_mean_forecast_error = np.mean(realVals - df['svr_time'])
    dtr_mean_forecast_error = np.mean(realVals - df['dtr_time'])
    lr_mean_forecast_error = np.mean(realVals - df['lr_time'])

    rf_mae = mean_absolute_error(realVals, df['rf_time'])
    svr_mae = mean_absolute_error(realVals, df['svr_time'])
    dtr_mae = mean_absolute_error(realVals, df['dtr_time'])
    lr_mae = mean_absolute_error(realVals, df['lr_time'])

    rf_mse = mean_squared_error(realVals, df['rf_time'])
    svr_mse = mean_squared_error(realVals, df['svr_time'])
    dtr_mse = mean_squared_error(realVals, df['dtr_time'])
    lr_mse = mean_squared_error(realVals, df['lr_time'])

    rf_rmse = np.sqrt(rf_mse)
    svr_rmse = np.sqrt(svr_mse)
    dtr_rmse = np.sqrt(dtr_mse)
    lr_rmse = np.sqrt(lr_mse)

    print("Forecast error: RF: {}, SVR: {}, DTR: {}, LR: {}".format(rf_forecast_error, svr_forecast_error, dtr_forecast_error, lr_forecast_error))
    print("Mean forecast error: RF: {}, SVR: {}, DTR: {}, LR: {}".format(rf_mean_forecast_error, svr_mean_forecast_error, dtr_mean_forecast_error, lr_mean_forecast_error))
    print("MAE: RF: {}, SVR: {}, DTR: {}, LR: {}".format(rf_mae, svr_mae, dtr_mae, lr_mae))
    print("MSE: RF: {}, SVR: {}, DTR: {}, LR: {}".format(rf_mse, svr_mse, dtr_mse, lr_mse))
    print("RMSE: RF: {}, SVR: {}, DTR: {}, LR: {}".format(rf_rmse, svr_rmse, dtr_rmse, lr_rmse))

    show_plot(df.index, realVals, df['rf_time'], df['svr_time'], df['dtr_time'], df['lr_time'])
    req_num_check(df)
    time_to_req_num(df)


if __name__ == '__main__':
    main()









