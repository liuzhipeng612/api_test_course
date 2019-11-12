#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: exercise.py
@Time: 2019-06-27 00:02
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import unittest


class Arithmetic:
    # def __init__(self, a, b):
    #     self.a = a
    #     self.b = b

    def add(self, a, b):
        return a + b

    def subs(self, a, b):
        return a - b


class TestDemo(unittest.TestCase):

    def test_add(self):
        pass

    def test_subs(self):
        pass


# import unittest
#
#
# class IntegerArithmeticTestCase(unittest.TestCase):
#     def testAdd(self):  # test method names begin with 'test'
#         self.assertEqual((1 + 2), 3)
#         self.assertEqual(0 + 1, 1)
#         pass
#
#     def testMultiply(self):
#         self.assertEqual((0 * 10), 0)
#         self.assertEqual((5 * 8), 40)
#         pass


if __name__ == '__main__':
    unittest.main()
