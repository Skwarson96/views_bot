import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error


def show_plot(index, real_vals, rf_vals, svr_vals, dtr_vals, lr_vals):

    plt.plot(index, real_vals)
    plt.plot(index, rf_vals)
    plt.plot(index, svr_vals)
    plt.plot(index, dtr_vals)
    plt.plot(index, lr_vals)
    plt.legend(['Real vals', 'RF vals', 'SVR vals', 'DTR vals', 'LR vals'])
    plt.show()


def req_num_check(dataframe, index, real_num, exp_num, threads_num):

    threads = threads_num.unique()
    print(threads)
    th_1 = dataframe.loc[dataframe['threads'] == threads[1]]

    forecast_error = th_1['real_req_num'].sum() - th_1['exp_req_num'].sum()
    mean_forecast_error = np.mean(th_1['real_req_num'] - th_1['exp_req_num'])
    mae = mean_absolute_error(th_1['real_req_num'] , th_1['exp_req_num'])
    mse = mean_squared_error(th_1['real_req_num'] , th_1['exp_req_num'])
    rmse = np.sqrt(mse)

    print('forecast_error: {}'.format(forecast_error))
    print('mean_forecast_error: {}'.format(mean_forecast_error))
    print('mae: {}'.format(mae))
    print('mse: {}'.format(mse))
    print('rmse: {}'.format(rmse))


    # plt.plot(index, real_num)
    # plt.plot(index, exp_num)
    # plt.legend(['Real num', 'Exp num'])
    # plt.show()


def main():

    print('test conclusions')

    # open test dataset

    df = pd.read_csv('test_dataset.csv')
    # print(df)

    df['exp_req_num'] = df['threads'] * df['iter_1'] * df['iter_2']
    # print(df)

    print(df.columns)
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

    # show_plot(df.index, realVals, df['rf_time'], df['svr_time'], df['dtr_time'], df['lr_time'])

    req_num_check(df, df.index, df['real_req_num'], df['exp_req_num'], df['threads'])

if __name__ == '__main__':
    main()









