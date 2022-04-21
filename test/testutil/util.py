from core.timeseries import TimeSeries
import numpy as np
import pandas as pd

def get_random_series(size,method='series'):
    dates = list(pd.date_range(start="4/2/2022", end="4/4/2022", periods=size))
    data = np.random.normal(size=size)
    if method == 'series':
        series_data = pd.Series(data=data, index=dates)
    elif method == 'numpy':
        series_data = np.array(np.array([dates,data]).T)
    return TimeSeries(series_data)

def get_random_pandas_series(size):
    dates = list(pd.date_range(start="4/2/2022", end="4/4/2022", periods=size))
    data = np.random.uniform(0,100,size=size)
    return pd.Series(data=data,index=dates)

def get_random_numpy_ndarray(size):
    dates = list(pd.date_range(start="4/2/2022", end="4/4/2022", periods=size))
    data = np.random.uniform(0,100,size=size)
    return np.array([(x,y) for x,y in zip(dates,data)])