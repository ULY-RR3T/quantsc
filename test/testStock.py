from core.stock import Stock
def testAdd():
    a = Stock("AAPL")
    b = Stock("GE")
    a.plot()
    b.plot()
    (a + b).plot()

def testSub():
    pass

def testMul():
    pass

if __name__ == "__main__":
    testAdd()
