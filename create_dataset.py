import pandas as pd
import numpy as np



def create_train_dataframe():
    data_df = pd.DataFrame(columns=['threads', 'iter_1', 'iter_2', 'time'])
    first_row = [0, 0, 0, 0]
    data_df.loc[0] = first_row
    print(data_df)
    return data_df

def save_train_dataframe(data_df):
    data_df.to_csv('dataset.csv', index=False)

def read_train_dataset():
    data_df = pd.read_csv('dataset.csv')
    print(data_df)
    # return data_df

def create_test_dataframe():
    data_df = pd.DataFrame(columns=['threads', 'iter_1', 'iter_2', 'real_time', 'rf_time', 'svr_time', 'dtr_time', 'lr_time', 'real_req_num'])
    first_row = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    data_df.loc[0] = first_row
    print(data_df)
    return data_df

def save_test_dataframe(data_df):
    data_df.to_csv('test_dataset.csv', index=False)

def read_test_dataset():
    data_df = pd.read_csv('test_dataset.csv')
    print(data_df)
    # return data_df

# data = create_train_dataframe()
# save_train_dataframe(data)
# read_train_dataset()
#
# test_data = create_test_dataframe()
# save_test_dataframe(test_data)
read_test_dataset()



