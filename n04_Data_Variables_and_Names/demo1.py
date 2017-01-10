print int('300') + 400

x = 42
print x.imag
print x.__class__


y = 2.5
z = 2.5
print id(y)
print id(z)

x = ['foo', 'bar']
callable(x.append)
callable(x.__doc__)


y = ['a', 'b']
y.append('c')
y.__setitem__(0, 'aa')

s = 'This is a string'
print s.upper()
print s.lower()
print s.replace('This', 'That')
