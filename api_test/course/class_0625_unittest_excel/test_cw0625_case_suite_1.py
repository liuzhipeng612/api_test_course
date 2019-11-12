#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_cw0625_case_suite_1.py
@Time: 2019-06-29 22:19
@Desc: Jungle old monster
"""
import unittest

from interface_automation.class_0625_unittest_excel.test_cw0625_case_1 import TestAdd

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestAdd))

if __name__ == '__main__':
    unittest.main()
