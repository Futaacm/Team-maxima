N= input('N: ')
K= input('K ')
from random import sample
x= sample(range(1000), N)

x.sort()
print x
print( x[K-1], x[len(x)-K])
