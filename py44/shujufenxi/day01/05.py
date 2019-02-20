import numpy as np 
a = np.arange(1,9)
b = a.reshape((2,4))
print(a,b)

a[0]=9999
print(b)
c = b.ravel()
print(c)

d = b.flatten()
d[0]=111
print(d)

d.shape = (2,4)
print(d)
d.resize(2,2,2)
print(d)





