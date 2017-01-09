x = 'yes' if 42 else 'no'
#yes
x = 'yes' if [] else 'no'
#no

x = 1 < 2 and 'f' in 'foo'
#true

bools = False, True, True
all(bools)
#false
any(bools)
#true
