#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0604csv.py
@Time: 2019/6/7 11:41
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import csv

# 创建一个txt文本文件，以csv格式（数据之间以英文逗号分隔）来添加数据
# a.第一行添加如下内容：name,age,gender,hobby,motto

with open('csvFile.csv', 'w+', newline='') as csvFile1:
    writeContent = csv.writer(csvFile1)
    writeContent.writerow(['name', 'age', 'gender', 'hobby', 'motto'])
    csvFile1.seek(0, 0)
    for i in csv.reader(csvFile1):
        print(i)

# b.从第二行开始，每行添加具体信息，例如：
# 可优,17,男,臭美,Always Be Coding!
# 柠檬小姐姐,16,女,可优,Lemon is best!

with open('csvFile.csv', 'a+', newline='') as csvFile2:
    writeContent = csv.writer(csvFile2)
    writeContent.writerows([['可优', '17', '男', '臭美', 'Always Be Coding!'],
                            ['柠檬小姐姐', '16', '女', '可优', 'Lemon is best!']])
    csvFile2.seek(0, 0)
    for j in csv.reader(csvFile2):
        print(j)

# c.具体用户信息要求来自于一个嵌套字典的列表（可自定义这个列表），例如：
# person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
#               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}, ]
person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
with open('csvFile.csv', 'w+', newline='') as csvFile3:
    writeContent = csv.writer(csvFile3)
    writeContent.writerow(eval('person_info'))
    csvFile3.seek(0, 0)
    for k in csv.reader(csvFile3):
        print(k)
