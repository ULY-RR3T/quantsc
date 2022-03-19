import pandas as pd
import matplotlib.pyplot as plt
import datetime

import yahoo_fin.stock_info as si
#http://theautomatic.net/yahoo_fin-documentation/
#http://theautomatic.net/yahoo_fin-documentation/#methods

def QSC.Stock.plot_earnings(stock: str): #, earnings_date: datetime):
    #get earning_history (no specified date)

    stock_earning_history = si.get_earnings_history(stock)
    frame = pd.DataFrame.from_dict(stock_earning_history)
    return frame.plot(x="startdatetime", y="espactual")






