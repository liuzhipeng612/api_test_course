#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_cw0622_suite.py
@Time: 2019-06-28 01:10
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""

import unittest
from python_basics.class_15_unittest2.test_cw0622_method import TestExcel

# 1
suite = unittest.TestSuite()
suite.addTests([TestExcel('test_none'), TestExcel('test_equal')])
# # 2
# loaders = unittest.TestLoader()
# suite.addTest(loaders.loadTestsFromTestCase(TestExcel))
# # 3
# from python_basics.class_0622_unittest2 import test_cw0622_method
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_cw0622_method))

if __name__ == '__main__':
    unittest.main()
