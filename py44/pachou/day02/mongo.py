import pymongo


#创建数据库连接对象
conn = pymongo.MongoClient('0.0.0.0',27017)

#创建库对象
db = conn.spiderdb


#创建集合对象
myset = db.t1

#执行插入语句
myset.insert_one({'name':'Tom'})
print("ok")



'''
show dbs
use spiderdb
show collections
db.ti.find().pretty()
db.ti.find()
db.t1.count()
db.dropDatabase()
'''




