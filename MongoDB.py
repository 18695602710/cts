# encoding:utf-8
from pymongo import MongoClient
import time,re
client = MongoClient('127.0.0.1', 27017)  # 建立客户端对象
db = client.mydb  # 连接mydb数据库，没有则自动创建
myset = db.nick   # 使用test_set集合，没有则自动创建
option_input = input(u'请输入选项(直接回车即记录当前时间，其他增加其他时间记录):')
if option_input != '':
    day = input('please input date(19/09/01):')
    week = input('please input week(0-6):')
    work_time = input('please input work_time(12:59:16):')
    result1 = re.match('\d\d/\d\d/\d\d$', day)
    result2 = re.match('[0-6]$', week)
    result3 = re.match('\d{2}:\d\d:\d\d$', work_time)
    result_list = [result1,result2,result3]
    if None in result_list:
        assert False,u'日期/星期/时间的格式不正确'
else:
    day = time.strftime('%y/%m/%d', time.localtime(time.time()))
    week = time.strftime('%w', time.localtime(time.time()))
    work_time = time.strftime('%H:%M:%S', time.localtime(time.time()))
myset.insert_one({
    'date':day,
    'week':week,
    'home_time':work_time
})   # 插入一条数据，如果没出错那么说明连接成功
# 下面是遍历查询数据
for i in myset.find():
    print(i)