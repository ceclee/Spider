'''库:aid1811,集合:stuinfo,文档:唐伯虎'''
import pymongo

database = 'AID1811'
table = 'stuinfo'

# 创建连接对象
conn = pymongo.MongoClient('localhost',27017)
# 创建库对象
db = conn[database]
# 创建集合对象
myset = db[table]
# 执行插入语句
myset.insert_one({'name':'秋香'})

# >>>show dbs
# >>>use aid1811
# >>>show collections
# >>>db.stuinfo.find().pretty()
# >>>db.stuinfo.count()
# >>>db.dropDatabase()






