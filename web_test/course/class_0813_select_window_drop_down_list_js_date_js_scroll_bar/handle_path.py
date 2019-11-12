#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: handle_path.py
@Time: 2019/7/17 0:38
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import os


class HandlePath:
    """
    处理文件路径，供个模块调用
    """
    pass


# 获取根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 获取配置文件config目录
CONFIG_DIR = BASE_DIR
CONFIG_GREETINGS_FILE_PATH = os.path.join(CONFIG_DIR, 'greetings.conf')
CONFIG_WRITE_FILE_PATH = os.path.join(CONFIG_DIR, 'write.conf')

pass
