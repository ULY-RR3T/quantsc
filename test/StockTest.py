import quantsc as qsc
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

class TestStockLoad():
    def testLoadStockFromTickerNoInterval(self,ticker="AAPL"):
        print("b-------------testLoadStockFromTickerNoInterval")
        stock = qsc.Stock(ticker)
        print(stock)
        print("e-------------testLoadStockFromTickerNoInterval")



class TestStockOperations():

    def testChangeBackend(self):
        s = qsc.Stock("AAPL")
        s.plot()
        qsc.change_plot_backend('plotly')
        s.plot()

    def testAdd(self):
        apple = qsc.Stock("AAPL")
        blackberry = qsc.Stock("BB")
        appberry = apple + blackberry
        print(appberry.data)
        type(appberry)
        appberry.plot(backend='matplotlib')


    # def testAdd(self):
    #     a = Stock("AAPL").get_data()
    #     b = Stock("GE").get_data()
    #     c = a + b
    #     c.plot()

    def testSub(self):
        pass

    def testMul(self):
        pass

if __name__ == "__main__":
    # load_test = TestStockLoad()
    # load_test.testLoadStockFromTickerNoInterval("GE")
    # ge = qsc.Stock("GE",start="2022-1-1",end="2022-2-1")
    # apple = qsc.Stock("AAPL",start="2022-3-20",end="2022-4-21",interval='1d')
    blackberry = qsc.Stock("BB")
    blackberry.plot()
    # apple.plot()
    # blackberry.diff(70).plot()
    # appberry = apple ** blackberry
    # appberry.dropna().plot()
    # apple.arima(1,1,1)
    # a = (apple.diff(2) / blackberry)
    # print(a.close)
    # a.plot(backend='plotly',style='candle')
    # a.autocorr_plot()

    # a.plot(backend = 'plotly')
    # a.model_arima(2,2,1)


