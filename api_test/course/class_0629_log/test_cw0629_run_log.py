#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_cw0625_run_log_1.py
@Time: 2019-06-29 22:19
@Desc: Jungle old monster
"""
from interface_automation.class_0629_log import HTMLTestRunnerNew
from interface_automation.class_0629_log.test_cw0629_case_suite import suite

with open('test_resule.html', 'wb')as save_file:
    result = HTMLTestRunnerNew.HTMLTestRunner(stream=save_file, verbosity=2, title='四则运算测试用例报告',
                                              description='测试两数的四则运算',
                                              tester='刀刀')
    result.run(suite)
