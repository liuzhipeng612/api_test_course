#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: pytest_project
@File: handle_systype.py
@Time: 2019/9/20 5:02 下午
@Desc: Jungle old monster
"""

import platform


def HandleSystype():
    #  获取Python版本
    print("当前Python版本是{}".format(platform.python_version()))

    #   获取操作系统可执行程序的结构，，(’32bit’, ‘WindowsPE’)
    print("操作系统可执行程序的结构是{}".format(platform.architecture()))

    #   计算机的网络名称，’Jomer-PC’
    print("计算机的网络名称是{}".format(platform.node()))

    # 获取操作系统名称及版本号，’Windows-7-6.1.7601-SP1′
    print("操作系统名称及版本号{}".format(platform.platform()))

    # 计算机处理器信息，’Intel64 Family 6 Model 42 Stepping 7, GenuineIntel’
    print("计算机处理器信息{}".format(platform.processor()))

    # 获取操作系统中Python的构建日期
    print(platform.python_build())

    #  获取系统中python解释器的信息
    print("Python的构建日期{}".format(platform.python_compiler()))

    if platform.python_branch() == "":
        print(platform.python_implementation())
        print(platform.python_revision())
    print(platform.release())
    print(platform.system())
    print(platform.system())
    print(platform.uname())
    print(platform.version())
    # print platform.system_alias()
    #  获取操作系统的版本
    print("操作系统的版本{}".format(platform.version()))

    #  包含上面所有的信息汇总
    print("信息汇总{}".format(platform.uname()))


def UsePlatform():
    sysstr = platform.system()
    if (sysstr == "Windows"):
        print("Call Windows tasks")
    elif (sysstr == "Linux"):
        print("Call Linux tasks")
    else:
        print("Other System tasks")


if __name__ == "__main__":
    HandleSystype()

    UsePlatform()
