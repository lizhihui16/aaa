import numpy as np 
a = np.array([1,2,3,4,5,6,7,8,9])
f = np.array([True,False,True,False,True,False,True,False,True])
print(a[f])
print(a[a>3])



b = np.arange(100)
flag_a = b%3==0
flag_b = b%7==0
print(flag_a)
print(flag_b)
flag = np.any([flag_a,flag_b],axis=0)
print(b[flag])




















