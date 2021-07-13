import pandas as pd
import numpy as np



def create_dataframe():
    data_df = pd.DataFrame(columns=['threads', 'iter_1', 'iter_2', 'time'])
    first_row = [0, 0, 0, 0]
    data_df.loc[0] = first_row
    print(data_df)
    return data_df

def save_dataframe(data_df):
    data_df.to_csv('dataset.csv', index=False)

def read_dataset():
    data_df = pd.read_csv('dataset.csv')
    print(data_df)
    # return data_df


# data = create_dataframe()
# save_dataframe(data)
read_dataset()





