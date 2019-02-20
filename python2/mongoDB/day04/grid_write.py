from pymongo import MongoClient
import gridfs

#获取数据库对象
conn = MongoClient('localhost',27017)
db = conn.grid

#获取文件集合对象
fs = gridfs.GridFS(db)

with open("/home/tarena/aid1808/python2/mongoDB/mongod/ye.jpg","rb") as f:
    fs.put(f.read(),filename = 'aa.jpg')

conn.close()