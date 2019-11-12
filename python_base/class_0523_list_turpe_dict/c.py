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

person_info = [{"name": "可优", "age": 17, "gender": "男", "hobby": "臭美", "motto": "Always Be Coding!"},
               {"name": "柠檬小姐姐", "age": 16, "gender": "女", "hobby": "可优", "motto": "Lemon is best!"}]
for i in person_info:
    dictContent = {}
    for j in i.items():
        # print(j[0]+str(j[1]))
        dictContent[j[0]] = j[1]
    print(dictContent)
