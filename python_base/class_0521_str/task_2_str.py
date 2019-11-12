#!/usr/bin/env python
# coding=UTF-8
"""
@Author: 刀刀
@Contact: 1626202029
@Project: cautious_eureka
@File: task_2_str.py
@Time: 2019/5/22 0:42
@Desc: 字符串相关课程
"""

"""
    1、定义字符串I'm Lemon, I love Python automated testing！
    提示：使用双引号还是单引号呢？
"""
print("\n1、定义字符串I'm Lemon, I love Python automated testing！")
a = "I'm Lemon, I love Python automated testing！"
print(a + '\n' + '=' * 66)

"""
    2.把website = 'http://www.python.org'中的python字符串取出来
    提示：可以使用字符串切片
"""
print("\n2.把website = 'http://www.python.org'中的python字符串取出来")

# 1
print('\n#1')
b = "website = 'http://www.python.org'"
print(b[22:28])

# 2
print('\n#2')
website = 'http://www.python.org'
print(website[11:17] + '\n' + '=' * 66)

"""
    3.将给定字符串前后的空格除去，把PHP替换为Python
    best_language = "     PHP is the best programming language in the world!      "。左右各有一个空格。
"""
print("\n3.将给定字符串前后的空格除去，把PHP替换为Python")
# 1
print('\n#1')
c = 'best_language = " PHP is the best programming language in the world! "'
d = c[0:17]
e = c[17:-1]
f = e.strip().replace('PHP', 'Python')
g = f.lstrip()
h = c[-1]
print(d + g + h)

# 2
print('\n#2')
best_language = " PHP is the best programming language in the world! "
print(best_language.strip().lstrip().replace('PHP', 'Python') + '\n' + '=' * 66)

"""
4.演练字符串操作
my_hobby = "Never stop learning!"
说明：“位置”指的是字符所处的位置（比如位置1，指的是第一个字符“N”），“索引”指的是字符的索引值（比如索引0， 代表的是第一个字符“N”）
"""
print("\n4.演练字符串操作")
my_hobby = "Never stop learning!"

print("\n# 截取从 位置2 ~ 位置6 的字符串")
print(my_hobby[1:6])

print("\n# 截取从 位置2 ~ 末尾 的字符串")
print(my_hobby[1:])

print("\n# 截取从 开始位置~ 位置6 的字符串")
print(my_hobby[:6])

print("\n# 截取完整的字符串")
print(my_hobby[:])

print("\n# 从索引3 开始，每2个字符中取一个字符")
print(my_hobby[3::2])

print("\n# 截取从 索引2 ~ 末尾-1的字符串")
print(my_hobby[2:-1])

print("\n# 截取字符串末尾两个字符")
print(my_hobby[-2:])

print("\n# 字符串的逆序（拓展）")
print(my_hobby[::-1] + '\n' + '=' * 66)

"""
5.去生鲜超市买橘子
收银员输入橘子的价格，单位：元／斤
收银员输入用户购买橘子的重量，单位：斤
计算并且 输出 付款金额
思考：如果输入的不是一个数字，执行程序会怎样？如何解决呢？
"""
print("\n5.去生鲜超市买橘子")
price = input("Please input price: ")
quantity = input("Please input quantity: ")
money = int(price) * int(quantity)
print("用户购买了{}斤，{}元/斤的橘子，总价{}元".format(price, quantity, money))
print("用户购买了%s斤，%s元/斤的橘子，总价%s元" % (price, quantity, money))
print("答：程序需要做异常处理，如果输入非数字程序不能识别，会抛出异常，需要将能够给用户理解的异常信息返回给用户。" + '\n' + '=' * 66)

"""
6.个人信息展示
在控制台依次提示用户输入：姓名、网名、年龄、性别、爱好、座右铭
按照以下格式输出：
**************************************************
个人信息展示
​
姓名（网名）
​
年龄：年龄
性别：性别
爱好：爱好
座右铭：座右铭
**************************************************
"""
name = input("Please input your name：")
screen_name = input("Please input your screen_name：")
age = input("Please input your age：")
gender = input("Please input your gender：")
hobbies = input("Please input your hobbies：")
motto = input("Please input your motto：")

# 1
print('*' * 66 + '\n' + '个人信息展示')
print('\n' + name + '(' + screen_name + ')' + '\n')
print('年龄：' + age)
print('性别：' + gender)
print('爱好：' + hobbies)
print('座右铭：' + motto)
print('*' * 66)

# 2
print('*' * 66 + "\n个人信息展示\n\n%s(%s)\n\n年龄：%s\n性别：%s\n爱好：%s\n座右铭：%s\n" % (
    name, screen_name, age, gender, hobbies, motto) + '*' * 66)

# 3
print('*' * 66 + "\n个人信息展示\n\n{}({})\n\n年龄：{}\n性别：{}\n爱好：{}\n座右铭：{}\n".format(
    name, screen_name, age, gender, hobbies, motto) + '*' * 66)
