from csv import reader


f = open('us_cities.txt')
print f.next()
print f.next()
print next(f)
print f.next()

e = enumerate(['foo', 'bar'])
print next(e)
print next(e)

f = open('test_table.csv', 'r')
nikkei_data = reader(f)
f.next()


x = [10, -10]
y = iter(x)
print type(y)


