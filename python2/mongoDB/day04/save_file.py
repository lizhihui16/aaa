from pymongo import MongoClient
import bson.binary 

conn = MongoClient('localhost',27017)
db = conn.image
myset = db.flower 

# #存储图片
# f = open('/home/tarena/aid1808/python2/mongoDB/mongod/ye.jpg','rb')
# data = f.read()

# #将数据转换为mongdb存储格式
# content = bson.binary.Binary(data)

# #插入到集合
# myset.insert({'filename':'flower.jpg','data':content})


#文件提取
img = myset.find_one({'filename':'flower.jpg'})

#将data域内容写入本地文件
with open('mm.jpg','wb') as f:
    f.write(img['data'])


conn.close()
