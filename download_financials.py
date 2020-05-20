import urllib.request
import csv

tickerList = []
with open('spTop50.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t')
    for row in spamreader:
        tickerList.append(row[0])
tickerList.pop(0)
print(tickerList)
for ticker in tickerList:

    try:
        # For Python 3.0 and later
        from urllib.request import urlopen
    except ImportError:
        # Fall back to Python 2's urllib2
        from urllib2 import urlopen

    #Downloads income statement
    print('Beginning income statement download with urllib2...')
    url = ("https://financialmodelingprep.com/api/v3/financials/income-statement/" + ticker + "?datatype=csv")
    urllib.request.urlretrieve(url, '/Users/belengayta/Downloads/income' + ticker +'.csv')

    #Downloads balance sheet statement
    print('Beginning balance sheet statement download with urllib2...')
    url = ("https://financialmodelingprep.com/api/v3/financials/balance-sheet-statement/" + ticker + "?datatype=csv")
    urllib.request.urlretrieve(url, '/Users/belengayta/Downloads/balance' + ticker +'.csv')

    #Downloads cash flows statement
    print('Beginning cash flow statement download with urllib2...')
    url = ("https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/" + ticker + "?datatype=csv")
    urllib.request.urlretrieve(url, '/Users/belengayta/Downloads/cashFlow' + ticker +'.csv')
