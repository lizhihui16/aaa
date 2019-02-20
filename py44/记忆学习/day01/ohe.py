import numpy as np


raw_samples=np.array([
    [1,3,2],
    [7,5,3],
    [1,8,6],
    [7,3,9]
])

code_tables = []
for col in raw_samples.T:
    #针对特定列的字典
    code_table={}
    for val in col:
        code_table[val]=None
        #将该列的编码字典加到编码字典列表中
    code_tables.append(code_table)
#填写编码字典列表中每个编码字典的值
for code_table in code_tables:
    size = len(code_table)

    for one,key in enumerate(sorted(code_table.keys())):
        code_table[key]=np.zeros(shape=size,dtype=int)
        code_table[key][one] = 1
ohe_samples = []
for raw_sample in raw_samples:
    ohe_sample=np.array([],dtype=int)
    for i,key in enumerate(raw_sample):
        ohe_sample=np.hstack((ohe_sample,code_tables[i][key]))
    ohe_samples.append(ohe_sample)
ohe_samples=np.array(ohe_samples)
print(ohe_samples)


