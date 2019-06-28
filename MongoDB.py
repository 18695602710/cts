# encoding:utf-8
from pymongo import MongoClient
import time
client = MongoClient('127.0.0.1', 27017)  # 建立客户端对象
db = client.mydb  # 连接mydb数据库，没有则自动创建
myset = db.nick   # 使用test_set集合，没有则自动创建
day = time.strftime('%y/%m/%d', time.localtime(time.time()))
week = time.strftime('%w', time.localtime(time.time()))
work_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
myset.insert({
    'date':day,
    'week':week,
    'home_time':work_time
})   # 插入一条数据，如果没出错那么说明连接成功
# 下面是遍历查询数据
for i in myset.find():
    print(i)