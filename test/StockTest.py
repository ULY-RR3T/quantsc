import qsc

class TestStockLoad():
    def testLoadStockFromTickerNoInterval(self,ticker="AAPL"):
        print("b-------------testLoadStockFromTickerNoInterval")
        stock = qsc.Stock(ticker)
        print(stock)
        print("e-------------testLoadStockFromTickerNoInterval")


class TestStockOperations():
    def testAdd(self):
        a = qsc.Stock("AAPL")
        b = qsc.Stock("GE")
        a.plot()
        b.plot()
        (a + b).plot()


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
    load_test = TestStockLoad()
    load_test.testLoadStockFromTickerNoInterval("GE")
