import pandas as pd

def read_stock(filename: str, columnNames = [], fileType = "csv"):
    stocks = {}
    if (fileType == "csv"):
        stocks = pandas.read_csv(filename)
    elif (fileType == "excel"):
        stocks = pandas.read_excel(filename)

    if not stocks:
        print("Failed to read " + filename)
        return

    stockList = []

    if columnNames:
        # reorder to match the correct columnNames
        # reset stocks[i] = corrected version of columnNames

    for i in dictOfStocks:
        s = Stock(dictOfStocks[i])
        stockList.append(s)

    return stockList
