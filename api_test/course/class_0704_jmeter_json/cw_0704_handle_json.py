#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0704_handle_json.py
@Time: 2019-07-07 17:04
@Desc: Jungle old monster
"""
import json

# 1、json对象结构
data_json = '{"status":1,"code":10001,"data":null,"msg":"登录成功"}'

# 2、将json格式的数据转换成为python中的字典类型
data_to_dict = json.loads(data_json)

# 3、dict对象结构
data_dict = {'name': '刀刀', 'height': 173, 'age': None, None: True}

# 4、将python中的字典类型转换成json格式的数据结构
data_to_json = json.dumps(data_dict)

# 5、json array对象结结构
data_json_array = '[{"status":1,"code":10001,"data":null,"msg":"登录成功"},' \
                  '{"status":1,"code":10001,"data":null,"msg":"登录成功"},' \
                  '{"status":1,"code":10001,"data":null,"msg":"登录成功"}]'

# 6、将json array数据结构转换成python中的列表嵌套字典类型
data_json_array_to_dict = json.loads(data_json_array)

# 7、python中的列表嵌套字典类型
data_list_dict = [{'status': 1, 'code': 10001, 'data': None, 'msg': '登录成功'},
                  {'status': 1, 'code': 10001, 'data': None, 'msg': '登录成功'},
                  {'status': 1, 'code': 10001, 'data': None, 'msg': '登录成功'}]
# 8、将python中的列表嵌套字典类型转换成json数组类型
data_list_dict_to_json = json.dumps(data_list_dict)

# 9、读取文本数据，确认是json数据格式的转换为dict或list嵌套dict，其他格式全部转换成json
with open('cw_0704_handle_json_dict.txt', encoding='utf-8')as jd_file:
    read_data = jd_file.readlines()
    for i in read_data:
        n = 'null'
        if n in i:
            file_to_dict = json.loads(i)
            if '[' in i:
                print('这是一个嵌套了字典的列表：', file_to_dict)
            else:
                print('这是一个字典：', file_to_dict)
        else:
            file_to_dict = eval(i)
            file_to_json = json.dumps(file_to_dict)
            print('这是一个json：', file_to_json)

# 读取文件json文件，转换成python中的字典类型
with open('cw_0704_handle_json.txt', encoding='utf-8')as json_file:
    data_dict_json = json.load(json_file)

# 将python中的字典数据转换成json数据格式并存储在文件
data_dict = {'name': '刀刀', 'height': 173, 'age': None, None: True}
with open('cw_0704_handle_json_write.txt', mode='w', encoding='utf-8')as dict_file:
    data_json = json.dump(data_dict_json, dict_file, ensure_ascii=False, indent=2)
