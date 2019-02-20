import numpy as np 

# a = np.array([[1,2,3],[4,5,6]])
# print(a)

# print(a.shape)

# print(a.size)
# print(len(a))

ary = np.arange(1,28)

ary.shape = (3,3,3)
# print(ary,ary.shape)
# print(ary[0])
# print(ary[0][0])
# print(ary[0][0][0])
# print(ary[0,0,0])
for i in range(ary.shape[0]):
    # print(ary[i])
    for j in range(ary.shape[1]):
        print(ary[j])
        for k in range(ary.shape[2]):
            print(ary[i,j,k,],end=' ')





# ary = np.arange(1,65)

# ary.shape = (4,4,4)
# print(ary,ary.shape)






