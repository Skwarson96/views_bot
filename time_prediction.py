import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


def clear_dataset():
    pass


def time_pred(thred_num, iter_1_num, iter_2_num):
    # print('test time pred')

    data_df = pd.read_csv('dataset.csv')

    # print(data_df)

    y = data_df.loc[:, 'time'].values
    X = data_df.loc[:, ['threads', 'iter_1', 'iter_2']].values
    # print(X)

    regr = RandomForestRegressor(random_state=0)
    regr.fit(X, y)

    pred_value = regr.predict([[thred_num, iter_1_num, iter_2_num]])

    return pred_value




