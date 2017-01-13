import urllib.request
import pandas as pd
from pandas_datareader import data,wb
import matplotlib.pyplot as plt
import datetime as dt  # Standard Python date / time library


url = 'http://research.stlouisfed.org/fred2/series/UNRATE/downloaddata/UNRATE.csv'
source = urllib.request.urlopen(url).read().decode('utf-8').split("\n")

print(source[0])
print(source[1])
print(source[2])

data = pd.read_csv(source, index_col=0, parse_dates=True, header=None)
print(type(data))
print(data.head())
print(data.describe())

# NEW


start, end = dt.datetime(2006, 1, 1), dt.datetime(2012, 12, 31)

data = data.DataReader('UNRATE', 'fred', start, end)

print(type(data))

data.plot()

plt.show()


