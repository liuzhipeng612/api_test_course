#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: c.py
@Time: 2019/5/22 1:39
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
csvFile = open('csvFormat.txt', 'a+', encoding='utf-8')
person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
listContent = []
for i in person_info:
    dictContent = {}
    for j in i.items():
        dictChild = dictContent[j[0]] = str(j[1])
        csvFile.write(eval('dictChild'))
    listContent.append(dictContent)
print(listContent)
# d.将所有用户信息写入到txt文件中之后，然后再读出
csvFile.seek(0, 0)
print(csvFile.read())
csvFile.close()
