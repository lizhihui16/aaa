
import numpy as np 
data = [
    ('zs',[10,15,8,2],3),
    ('ls',[30,65,44,3],43),
    ('ww',[60,25,2,6],13),
    ('ww',[60,25,2,8],13),

]
#第一种
# a = np.array(data,dtype='U2,4int32,int32')
# print(a,a[0]['f2'])


# #第二种
# b = np.array(data,dtype=[('name','str_',2),('scores','int32',4),('age','int32',1)])
# print(b,b[0]['age'])

# #第三种
# c=np.array(data,dtype={'names':['name','scores','age'],'formats':['U2','4int32','int32']})
# print(c,c[1]['name'])

# #第四种
# d = np.array(data,dtype={'name':('U2',0),'scores':('4int32',16),'age':('int32',32)})
# print(d[0]['age'])

# #第五种
# e = np.array([0x1234,0x5678],dtype=('u2',{'lowc':('u1',0),'highc':('u1',1)}))
# print('%x'%e[0])
# print('%x'%e['lowc'][0])
# print('%x'%e['highc'][0])





f = np.array(['2018','2019-02-01','2019-03-01','2019-01-02 01:01:01'])

g=f.astype('M8[D]')
print(g,g.dtype)

h = g.astype('int32')
print(h)
print(h[2]-h[1])


