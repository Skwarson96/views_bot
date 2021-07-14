import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import pickle

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

from sklearn import svm
from sklearn import tree

def show_plots(df, max_val):

    var = 'threads'
    data = pd.concat([df['time'], df[var]], axis=1)
    data.plot.scatter(x=var, y='time', ylim=(0, max_val))

    var = 'iter_1'
    data = pd.concat([df['time'], df[var]], axis=1)
    data.plot.scatter(x=var, y='time', ylim=(0, max_val))

    var = 'iter_2'
    data = pd.concat([df['time'], df[var]], axis=1)
    data.plot.scatter(x=var, y='time', ylim=(0, max_val))

    plt.show()

def clear_dataset(df):

    # print(df)
    max_val = df['time'].max()

    # show_plots(df, max_val)

    # Remove global outlaiers
    range_ = 2000
    df = df.drop(df[df['time'] > range_].index)
    # show_plots(df, max_val)

    # Remove outlaiers for each thread
    threads_list = df['threads'].unique()
    # print(threads_list)
    df = df.sort_values(by=['threads'])
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    df_copy = df.copy()
    df_copy = df.iloc[0:0]

    for thread_num in threads_list:

        df_part = df.loc[lambda df: df['threads'] == thread_num]
        max_val = df_part['time'].max()
        # print(max_val)
        df_part = df_part.drop(df_part[df_part['time'] > max_val-100].index)

        df_copy = pd.concat([df_copy, df_part], ignore_index=True)

    # print(df_copy)
    # show_plots(df_copy, 2000)

    return df_copy

# def save_regressors():
#     pass

def train_regressors(thred_num, iter_1_num, iter_2_num):


    # raw dataset
    data_df = pd.read_csv('dataset.csv')

    y = data_df.loc[:, 'time'].values
    X = data_df.loc[:, ['threads', 'iter_1', 'iter_2']].values

    regr_rf = RandomForestRegressor(random_state=0)
    regr_rf.fit(X, y)

    pickle.dump(regr_rf, open('./regressors/reg_RF.p', 'wb'))


    regr_svr = svm.SVR()
    regr_svr.fit(X, y)
    pickle.dump(regr_svr, open('./regressors/reg_SVR.p', 'wb'))



def load_model():
    pass




def time_pred(thred_num, iter_1_num, iter_2_num):

    # raw dataset
    data_df = pd.read_csv('dataset.csv')

    y = data_df.loc[:, 'time'].values
    X = data_df.loc[:, ['threads', 'iter_1', 'iter_2']].values

    regr = RandomForestRegressor(random_state=0)
    regr.fit(X, y)

    pred_value = regr.predict([[thred_num, iter_1_num, iter_2_num]])

    # clear dataset
    clear_df = clear_dataset(data_df)

    y = clear_df.loc[:, 'time'].values
    X = clear_df.loc[:, ['threads', 'iter_1', 'iter_2']].values

    regr_2 = RandomForestRegressor(random_state=0)
    regr_2.fit(X, y)

    pred_value_2 = regr_2.predict([[thred_num, iter_1_num, iter_2_num]])


    return pred_value, pred_value_2



