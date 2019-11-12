#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0528.py
@Time: 2019/5/29 22:38
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

# 1.编写如下程序
"""
a.用户输入1-7七个数字，分别代表周一到周日
b.如果输入1~5，打印对应的“周一”~“周五”，如果输入的数字是6或7，打印输出“周末”
c.如果输入0，退出循环
d.输入其他内容，提示：“输入有误，请重新输入！”
提示：本题可以使用if和while循环，同时需要校验用户的输入是否正确
"""
while True:
    week = input("请输入1-7的整数：")
    if not week.isdigit():
        print("输入有误，请重新输入！")
    else:
        week = int(week)
        if week == 0:
            break
        elif week == 1:
            print("周一")
        elif week == 2:
            print("周二")
        elif week == 3:
            print("周三")
        elif week == 4:
            print("周四")
        elif week == 5:
            print("周五")
        elif week == 6 or week == 7:
            print("周末")
        else:
            print()

# 2.编写如下程序
"""
输入一个人的身高(m)和体重(kg)，根据BMI公式（体重除以身高的平方）计算他的BMI指数
a.例如：一个65公斤的人，身高是1.62m，则BMI为 :  65 / 1.62 ** 2 = 24.8
b.根据BMI指数，给与相应提醒
低于18.5： 过轻 18.5-25：   正常 25-28：      过重 28-32：      肥胖 高于32：   严重肥胖
"""


def num(types, nums):
    """判断输入文本是否整数或浮点数，直到输入正确并返回浮点数"""
    while not (nums.isdigit() or nums.replace(".", "").isdigit()):
        print("输入有误，请重新输入！")
        nums = input("请输入{}：".format(types))
    return float(nums)


def bmi(weights, heights):
    """判断体重类型"""
    bmis = weights / (heights ** 2)
    if bmis < 18.5:
        print("过轻")
    elif 18.5 <= bmis <= 25:
        print("正常")
    elif 25 <= bmis <= 28:
        print("过重")
    elif 28 <= bmis <= 32:
        print("肥胖")
    elif bmis > 32:
        print("严重肥胖")
    else:
        print()


while True:
    """循环输入身高和体重"""
    height = input("请输入{}：".format("身高"))
    height = num("身高", height)
    weight = input("请输入{}：".format("体重"))
    weight = num("体重", weight)
    bmi(weight, height)
    continue

# while True:
#     height = input("请输入{}：".format("身高"))
#     height = num("身高", height)
#     weight = input("请输入{}：".format("体重"))
#     weight = num("体重", weight)
#     bmi = weight / (height ** 2)
#     if bmi < 18.5:
#         print("过轻")
#     elif 18.5 <= bmi <= 25:
#         print("正常")
#     elif 25 <= bmi <= 28:
#         print("过重")
#     elif 28 <= bmi <= 32:
#         print("肥胖")
#     elif bmi > 32:
#         print("严重肥胖")
#     else:
#         continue

# 3.编写如下程序
"""
从键盘输入一个用户名和密码，判断是否正确，如果正确则打印登录系统成功，否则显示用户名或密码错误。
a.定义一个函数，接收用户输入的用户名和密码作为参数
b.正确的账号，用户名为lemon，密码为best
"""


def user(u_names, p_words):
    if u_names == 'lemon' and p_words == 'best':
        print('登录系统成功')
    else:
        print('用户名或密码错误')


username = input('请输入用户名：')
password = input('请输入密码：')

user(username, password)

# 4.取出列表中最大的值
# 将列表[13, 20, 42, 85, 9, 45]中的最大值为85
nums = [13, 20, 42, 85, 9, 45]
nums.sort()
print(nums[-1])

# 二、选作题
# 1.列表去重    将列表[10, 1, 2, 20, 10, 3, 2, 1, 15, 20, 44, 56, 3, 2, 1]去除重复元素


# 2.编写如下程序  打印出1-100之间除了含7和7的倍数之外的所有数字


# 3.编写如下程序
"""
输入键盘数字键(0~9)，返回数字键上方字符
a.定义如下字典num_str_dic = {'1': '!', '2': '@', '3': '#', '4': '$','5': '%', '6': '^', '7': '&', '8': '*', '9': '(', '0': ')'}
b.例如：键盘输入5，程序输出%
c.键盘输入0~9，正常输出字符之后，退出程序，否则继续提示输入
"""
