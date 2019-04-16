'''建库:AID1811db 建表:stuinfo'''
import pymysql
import warnings

# 数据库连接对象
db = pymysql.connect(
                    'localhost',
                    'root',
                    '123456',
                    charset='utf8')
# 游标对象
cursor = db.cursor()
# 执行sql命令
c_db = 'create database if not exists AID1811db charset utf8'
u_db = 'use AID1811db'
c_tab = 'create table if not exists stuinfo(name varchar(20))'
ins = 'insert into stuinfo values("Tom")'
# 忽略警告
warnings.filterwarnings('ignore')

cursor.execute(c_db)
cursor.execute(u_db)
cursor.execute(c_tab)
cursor.execute(ins)

# 提交到数据库执行
db.commit()
# 关闭
cursor.close()
db.close()

















