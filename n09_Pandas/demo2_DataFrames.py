import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('test_pwt.csv')
# print type(df)
# print df
#
# print df[2:5]
# print df[['country', 'tcgdp']]
# print df.ix[2:5, ['country', 'tcgdp']]

keep = ['country', 'POP', 'tcgdp']
df = df[keep].copy()
# print df

countries = df.pop('country')
# print type(countries)
# print countries
# print df
df.index = countries
# print df

df.columns = 'population', 'total GDP'
# print df
df['population'] *= 1e3
# print df
df['GDP percap'] = df['total GDP'] * 1e6 / df['population']
print df

# print df['GDP percap'].plot(kind='bar')
# plt.show()

df = df.sort_values(by="GDP percap", ascending=False)
print df

print df['GDP percap'].plot(kind='bar')
plt.show()


