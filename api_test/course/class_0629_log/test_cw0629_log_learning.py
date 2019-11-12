#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_cw0629_log_learning.py
@Time: 2019-07-05 01:13
@Desc: Jungle old monster
"""
import logging

# 定义日志收集器，指定收集器的名称，返回Logger对象
case_logger = logging.getLogger('case')

# 设置日志收集器等级
case_logger.setLevel(logging.DEBUG)

# 输出到console控制台
console_handle = logging.StreamHandler()

# 输出到日志文件
file_handle = logging.FileHandler('cases.log', encoding='utf-8')

console_handle.setLevel(logging.DEBUG)
file_handle.setLevel(logging.INFO)

# 定义日志显示格式，简单格式\复杂格式
simple_formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[msg]%(message)s')
verbose_formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[msg]%(message)s-%(filename)s-%(levelno)s')

# 关联并设置终端显示格式为简单模式
console_handle.setFormatter(simple_formatter)
# 关联并设置文件显示格式为复杂嘛事
file_handle.setFormatter(verbose_formatter)

# 对接显示器
case_logger.addHandler(console_handle)
case_logger.addHandler(file_handle)

if __name__ == '__main__':
    case_logger.debug('这个是一个debug级别的日志信息')
    case_logger.info('这个是一个info级别的日志信息')
    case_logger.warning('这个是一个warning级别的日志信息')
    case_logger.error('这个是一个error级别的日志信息')
    case_logger.critical('这个是一个critical级别的日志信息')
