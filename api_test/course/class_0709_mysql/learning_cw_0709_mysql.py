#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0709_mysql.py
@Time: 2019-07-11 00:26
@Desc: Jungle old monster
"""

import pymysql

from interface_automation.class_0709_mysql.cw_0709_config import do_config

host = do_config.get_value('mysql', 'host')
user = do_config.get_value('mysql', 'user')
password = do_config.get_value('mysql', 'password')
db = do_config.get_value('mysql', 'db')
port = do_config.get_int('mysql', 'port')
charset = do_config.get_value('mysql', 'charset')

# 链接数据库
conn = pymysql.connect(
    host=host,
    user=user,
    password=password,
    db=db,
    port=port,
    charset=charset,  # 编码只能写utf8
    cursorclass=pymysql.cursors.DictCursor  # 执行SQL的结果为字典类型
)
# 创建游标
cursor = conn.cursor()

# 执行SQL语句

# 1、SQL语句
sql = 'select * from member limit 0,10;'

# 2、执行语句
cursor.execute(sql)

# 3、提交执行
conn.commit()

# 获取执行结果

# 1、获取单行数据
result1 = cursor.fetchone()

# 2、获取所有数据，同一链接执行多条查询语句，只能从已被查数据库行数后面开始读取
result2 = cursor.fetchall()

pass
