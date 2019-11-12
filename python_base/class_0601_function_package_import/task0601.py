#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: task0601.py
@Time: 2019/6/4 0:48
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

# 什么是模块？有什么作用？
"""
答：
    1、py文件就是模块，
    2、同一个模块可以存储相关用途的函数、类等，用不同py可以清晰的对各种类别的函数、类等进行分类，方便调取。
"""
# 模块的导入方式有哪几种？
"""
答：
    1、from...import...
    2、from...import *
    3、from...import as
    4、import...
    5、import *
    6、import...as...
"""
# 什么是全局变量？ 什么是局部变量？
"""
答：
    相对于当前函数
    1、函数外的变量为全局变量
    2、函数内的变量为局部变量
"""
# 函数内部如何修改全局变量？
"""
答：使用global x
"""
# 新建一个包pack，在包中新建两个模块module1，module2,   在module1中定义一个函数，然后在module2中导入module1中定义的函数，并调用。
"""
答：
pack1
        __init__.py
        module1
            def mod():
                pass
        module2
            import module1 as mods
            mods.mod()
"""

# 有一个列表 heros = [ ['孙悟空','韩信'], ['后羿', '鲁班'], ['庄周','项羽']], 请将这个列表降维，称为扁平列表。最后结果
# [ '孙悟空','韩信', '后羿', '鲁班', '庄周','项羽'], 代码行数越少越好。

heros = [['孙悟空', '韩信'], ['后羿', '鲁班'], ['庄周', '项羽']]
print([heros[0][0], heros[0][1], heros[1][0], heros[1][1], heros[2][0], heros[2][1]])
print(heros[0] + heros[1] + heros[2])
