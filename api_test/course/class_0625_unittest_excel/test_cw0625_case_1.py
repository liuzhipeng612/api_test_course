#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_cw0625_case_1.py
@Time: 2019-06-29 22:18
@Desc: Jungle old monster
"""
import unittest

from interface_automation.class_0625_unittest_excel.cw0625_testing_object import Arithmetic


class TestAdd(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('\n{:=^40s}\n'.format('开始执行用例'))
        cls.file_name = 'demo.txt'
        print('打开【{}】文件\n'.format(cls.file_name))
        cls.file = open(cls.file_name, 'a', encoding='utf-8')
        cls.file.write('\n{:=^40s}\n'.format('开始执行用例'))

    @classmethod
    def tearDownClass(cls):
        print('关闭【{}】文件'.format(cls.file_name))
        print('\n{:=^40s}\n'.format('用例执行结束'))
        cls.file.write('\n{:=^40s}\n'.format('用例执行结束'))
        cls.file.close()

    def test_minus_add(self):
        real_result = Arithmetic(-2, -4).add()
        expect_result = -6
        msg = '测试两负数相加'
        try:
            self.assertEqual(expect_result, real_result, msg)
            self.file.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.file.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
            raise e

    def test_negative_positive_add(self):
        real_result = Arithmetic(-3, 4).add()
        expect_result = 1
        msg = '负数与正数相加'
        try:
            self.assertEqual(expect_result, real_result, msg)
            self.file.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.file.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
            raise e

    def test_zero_add(self):
        real_result = Arithmetic(0, 0).add()
        expect_result = 0
        msg = '零和零相加'
        try:
            self.assertEqual(expect_result, real_result, msg)
            self.file.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.file.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
            raise e

    def test_positive_add(self):
        real_result = Arithmetic(5, 3).add()
        expect_result = 8
        msg = '正数和正数相加'
        try:
            self.assertEqual(expect_result, real_result, msg)
            self.file.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.file.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
            raise e

    def test_positive_negative_add(self):
        real_result = Arithmetic(13, -2).add()
        expect_result = 11
        msg = '正数和负数相加'
        try:
            self.assertEqual(expect_result, real_result, msg)
            self.file.write('\n{},执行结果为:{}\n'.format(msg, 'Pass'))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.file.write('\n{},执行结果为:{}\n具体异常为:{}\n'.format(msg, 'Fail', e))
            raise e


if __name__ == '__main__':
    unittest.main()
