import quantsc as qsc

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
    # qsc.Stock("AAPL").plot()
    operations_test = TestStockOperations()
    # operations_test.testChangeBackend()
    operations_test.testAdd()
    # appberry.plot(backend='matplotlib')
