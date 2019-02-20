import numpy as np 
a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)
#垂直
# c = np.vstack((a,b))
# print(c)
# a,b = np.vsplit(c,2)
# print(a,'\n',b)

#水平
# d = np.hstack((a,b))
# print(d)
# a,b = np.hsplit(d,2)
# print(a,'\n',b)

#深度
# e = np.dstack((a,b))
# print(e)
# a,b = np.dsplit(e,2)
# print(a,'\n',b)

# a = a.reshape(2,3)
# b = b.reshape(2,3)
# print(a,'\n',b)
# c = np.concatenate((a,b),axis=0)
# print(c)

# print(np.split(c,2,axis=0))



a = np.arange(1,7)
b = np.arange(11,16)
c = np.pad(b,pad_width=(0,1),mode = 'constant',constant_values=-1)

print(a)
print(b)
print(c)







