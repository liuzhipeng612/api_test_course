#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_cw0625_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import unittest

from cases.test_01_register import ApiTest
from cases import test_01_register
from cases import test_02_login
from cases import test_03_recharge

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_03_recharge))

if __name__ == '__main__':
    unittest.main()
