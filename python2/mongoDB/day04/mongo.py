from pymongo import MongoClient

#创建数据库链接
conn = MongoClient('localhost',27017)

#创建数据库对象
db = conn.stu 

#创建集合对象
myset = db['class4']

#数据操作
# print(dir(myset))

# 插入文档
# myset.insert_many([{'name':'张铁林','King':'乾隆'},{'name':'张国立','King':'康熙'}])
# myset.insert_one({'name':'任贤齐','King':'令狐冲'})
# myset.insert({'name':'古天乐','role':'杨过'})
# myset.insert([{'name':'李若彤','role':'小龙女'},{'name':'刘亦菲','role':'王语嫣'}])
# myset.save({'name':'胡军','role':'萧峰'})
# myset.save({'_id':1,'name':'林志颖','role':'段誉'})
# myset.insert([{'name':'唐国强','role':'雍正'},{'name':'孙俪','role':'甄嬛'}])

#查找操作
# cursor = myset.find({'role':{'$exists':True}},{'_id':0})
# print(cursor)
# for i in cursor:
#     print(i['name'],'---',i['role'])
# print(cursor.next())   #打印下一条文档

# for i in cursor.limit(3):
#     print(i)

# for i in cursor.sort([('name',1),('role',-1)]):
#     print(i)

# dic = {'$or':[{'role':{'$exists':False}},{'name':'古天乐'}]}
# d = myset.find_one(dic)
# print(d)

# #修改操作
# myset.update_one({'King':{'$exists':True}},{'$set':{'name':'陈小春','King':'韦小宝'}})

# myset.update_many({'King':{'$exists':True}},{'$rename':{'King':'role'}})

# myset.update({'name':'张国立'},{'$set':{'name':'张卫健','role':'韦小宝'}}，multi=True)
# myset.update({'name':'张国立'},{'$set':{'name':'张卫健','role':'韦小宝'}})

# myset.update({'name':'高圆圆'},{'$set':{'role':'周芷若'}},upsert=True)

#删除操作
# myset.delete_one({'name':'高圆圆'})
# myset.delete_many({'role':'韦小宝'})
# myset.remove({'name':'林志颖'})

#复合操作
print(myset.find_one_and_update({'role':'萧峰'},{'$set':{'name':'黄日华'}}))
#关闭数据库链接
conn.close()