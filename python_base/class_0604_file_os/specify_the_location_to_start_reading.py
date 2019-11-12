#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: c.py
@Time: 2019/5/22 1:40
@Desc: 从指定行数或字符开始读取
"""


# 1.默认你知道“指定行”的行号
# 那么：
def appoint_line(num, file):
    with open(file, "r", encoding='utf-8') as f:
        out = f.readlines[num - 1]
        return out


print(appoint_line(2, "c:/text.txt"))


# 以上示例为读取c盘下的text.txt文件的第二行
# 2.假如所谓“指定行”为开头几个字符，这里假设为三个
def appoint_line(file):
    # appoimt_spring是指你指定行的前三个字符,你可以自行指定
    appoint_spring = input(">>").strip()
    with open(file, "r", encoding='utf-8') as f:
        for line in f.readlines():
            if line[0:3] == appoint_spring:
                return line


print(appoint_line("c:/text.txt"))
# 以上示例为根据你输入的所指定行的前三个字符打印出c盘下的text.txt文件下的“指定行”
