import pandas as pd
import numpy as np
from core import timeseries as ts
from core import Stock as stock
from datetime import datetime,timedelta
# from core import stock

#if __name__ == "__main__":
#    dates = pd.date_range(start="4/2/2022",end="4/4/2022",periods=3)
#    series_data = pd.Series(data=[1,2,3],index=dates)
#    print(series_data)

    # test_series = timeseries("AAPL")
    # test_series.load_data()
#

if __name__ == "__main__":
    dates2 = ["10/20/2003", "10/20/2004", "10/20/2005", "10/20/2006", "10/20/2007"]
    values2 = [3, 1, 4, 1, 5]
    data2 = np.array([values2, dates2])
    jq_series = ts.TimeSeries()
    jq_series.load_data(data2)
    print(data2)
    print(jq_series)