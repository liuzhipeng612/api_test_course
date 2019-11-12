#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test2.py
@Time: 2019-07-28 23:37
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

import re


class Context:
    @classmethod
    def mobilephone(cls, data):
        pattern = r'\${not_existed_tel}'
        repl = getattr(cls, 'existed')
        string = data
        if re.search(pattern, string):
            new_data = re.sub(pattern, repl, string)
            return new_data
        else:
            return string
