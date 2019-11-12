#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: test_cw0622_run.py
@Time: 2019-06-28 01:22
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import unittest
from python_basics.class_15_unittest2 import test_cw0622_suite

runner = unittest.TextTestRunner()
runner.run(test_cw0622_suite.suite)
