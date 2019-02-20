import numpy as np 
a = np.array([[1+1j,2+4j,3+6j],[3+7j,2+4j,6+66j],[9+2j,4+4j,9+6j]])
print(a.dtype,a.ndim)
print(a.real)
print(a.imag)
print(a.imag.T)

c= a[:,:2]
print(c)
print(c.T)

print([e for e in a.flat])


