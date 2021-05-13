#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pymysql

conn = pymysql.connect(host="127.0.0.1", user="root", password="root1234", database="django_test", charset="utf8")

cursor = conn.cursor()

sql = "select create_date,recharge_user_num,recharge_amount_num from app_demo_dayrechargeuseramount"

cursor.execute(sql)

res = cursor.fetchall()

create_date_lst = []
recharge_user_num_lst = []
recharge_amount_num_lst = []

for line in res:
    create_date, recharge_user_num, recharge_amount_num = line[0], line[1], line[2]
    # print(create_date, recharge_user_num, recharge_amount_num)
    create_date_lst.append(create_date)
    recharge_user_num_lst.append(recharge_user_num)
    recharge_amount_num_lst.append(recharge_amount_num)

print(create_date_lst)
print(recharge_user_num_lst)
print(recharge_amount_num_lst)

# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
