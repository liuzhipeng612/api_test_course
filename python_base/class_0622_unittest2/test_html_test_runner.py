#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_html_test_runner.py
@Time: 2019/6/29 19:19
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
from python_basics.class_15_unittest2 import HTMLTestRunnerNew
from python_basics.class_15_unittest2 import test_cw0622_suite

with open('test_report.html', 'wb+') as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file, title='测试报告', description='excel判断对错',
                                              tester='刀刀', verbosity=2)
    runner.run(test_cw0622_suite.suite)
