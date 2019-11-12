#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0523.py
@Time: 2019/5/24 0:34
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
# 1、删除如下列表中的"矮穷丑"，写出能想到的所有方法
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]

# 1
info.remove("矮穷丑")
print(info)

# 2
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
info.pop(3)
print(info)

# 3
info = ["yuze", 18, "男", "矮穷丑", ["高", "富", "帅"], True, None, "Always Be Coding"]
del info[3]
print(info)

# 2、什么时候用列表、什么时候用元组、什么时候用字典？他们分别适合什么场景使用？
print(
    """
    答：1）需要增删改数据集的时候采用列表
        2）只希望使用固定的数据集，不需要更改数据的时候采用元组
        3）需要使用键值对的时候用字典
        3）允许用户交互，提交修改删除数据的场景下使用，如：网站用户中心
        4）只允许用户查看数据的场景下使用，如：查看统计报表
        5）需要序列化数据的场景下使用，如统计用户信息
    """
)
# 3、有5道小题：

# a、某相亲节目需要获取你的个人信息，请存储你的：姓名、性别、年龄

# 1 列表
manInfoList = ['土刀子', '男', 31]
print(manInfoList)

# 2 元组
manInfoTuple = ('土刀子', '男', 31)
print(manInfoTuple)

# 3 字典
manInfoDict = {'姓名': '土刀子', '性别': '男', '年龄': 31}
print(manInfoDict)

# 4 集合
manInfoSet = {'土刀子', '男', 31}
print(manInfoSet)

# b、有一个人对你很感兴趣，平台需要您补足您的身高和联系方式；
# 1 list.append()
manInfoList1 = ['土刀子', '男', 31]
manInfoList2 = manInfoList1.append(173)
manInfoList3 = manInfoList1.append(17322322629)
print(manInfoList1)

# 2 list.extend()
manInfoList4 = ['土刀子', '男', 31]
manInfoList5 = [173, 17322322629]
manInfoList6 = manInfoList4.extend(manInfoList5)
print(manInfoList4)

# 3 dict
manInfoDict1 = {'姓名': '土刀子', '性别': '男', '年龄': 31}
manInfoDict2 = manInfoDict1['身高'] = 173
manInfoDict3 = manInfoDict1['联系方式'] = 17322322629
print(manInfoDict1)

# c、平台为了保护你的隐私，需要你删除你的联系方式；

# 1 list.remove()
manInfoList1.remove(17322322629)
print(manInfoList1)

# 2 dict修改为空
manInfoDict1['联系方式'] = ''
print(manInfoDict1)

# 3 dict.pop()
manInfoDict4 = {'姓名': '土刀子', '性别': '男', '年龄': 31, '身高': 173, '联系方式': 17322322629}
manInfoDict4.pop('联系方式')
print(manInfoDict4)

# d、你为了取得更好的成绩，需要取一个花名，并修改自己的身高和其他你觉得需要改的信息。

# 1 list.append() list[x]
manInfoList1.append('刀刀')
print(manInfoList1)
manInfoList1[3] = '185'
print(manInfoList1)
manInfoList1[2] = 18
print(manInfoList1)

# 2 list.insert(index,object)
manInfoList7 = ['土刀子', '男', 31, 173]
manInfoList7.insert(1, '刀刀')
print(manInfoList7)

# 3 dict.update()
manInfoDict5 = {'昵称': '刀刀', '年龄': 18, '身高': 185}
manInfoDict4.update(manInfoDict5)
print(manInfoDict4)

# e、你进一步添加自己的兴趣，至少需要 3 项。一经确定，不可修改。

# 1 list.insert(index,tuple)
manInfoTuple1 = ('唱歌', '跳舞', '玩游戏')
manInfoList1.insert(5, manInfoTuple1)
print(manInfoList1)

# 2
manInfoDict4['兴趣'] = manInfoTuple1
print(manInfoDict4)
