# !/usr/bin/env python
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
from configparser import ConfigParser

from ddt import ddt, data

from interface_automation.class_0629_log.cw0629_testing_object import Arithmetic
from interface_automation.class_0629_log.test_cw0629_excel_package import HandleExcel
from interface_automation.class_0629_log.test_cw0629_log import do_logger

config = ConfigParser()
config.read('class_0629.conf', encoding='utf-8')
# file = config['file path']['case_path']
file = config.get('file path', 'case_path')
true_result = config.get('msg', 'true_result')
fail_result = config.get('msg', 'fail_result')


@ddt
class TestArithmetic(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('开始执行用例'))

    @classmethod
    def tearDownClass(cls):
        do_logger.info('\n{:=^40s}\n'.format('用例执行结束'))

    def setUp(self):
        pass

    def tearDown(self):
        wb, ws = self.my_HandleExcel.load_excel()
        wb.save(file)
        wb.close()

    @data(*HandleExcel(file, 'add').get_case())
    def test_add(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'add')
        case_id, title, l_data, r_data, expected = case_list['case_id'], case_list['title'], case_list['l_data'], \
                                                   case_list['r_data'], case_list['expected']
        actual = Arithmetic(l_data, r_data).add()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_id + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_id + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e

    @data(*HandleExcel(file, 'minus').get_case())
    def test_minus(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'minus')
        case_id, title, l_data, r_data, expected = case_list['case_id'], case_list['title'], case_list['l_data'], \
                                                   case_list['r_data'], case_list['expected']
        actual = Arithmetic(l_data, r_data).minus()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_id + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_id + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e

    @data(*HandleExcel(file, 'multiply').get_case())
    def test_multiply(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'multiply')
        case_id, title, l_data, r_data, expected = case_list['case_id'], case_list['title'], case_list['l_data'], \
                                                   case_list['r_data'], case_list['expected']
        actual = Arithmetic(l_data, r_data).multiply()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_id + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_id + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e

    @data(*HandleExcel(file, 'division').get_case())
    def test_division(self, case_list):
        self.my_HandleExcel = HandleExcel(file, 'division')
        case_id, title, l_data, r_data, expected = case_list['case_id'], case_list['title'], case_list['l_data'], \
                                                   case_list['r_data'], case_list['expected']
        actual = Arithmetic(l_data, r_data).division()
        result = expected
        msg = title
        try:
            self.assertEqual(result, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
            self.my_HandleExcel.write_result(case_id + 1, actual, true_result)
            do_logger.error("{}, 执行结果为: {}".format(msg, true_result))
        except AssertionError as e:
            print('具体异常为{}'.format(e))
            self.my_HandleExcel.write_result(case_id + 1, actual, fail_result)
            do_logger.error("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))
            raise e


if __name__ == '__main__':
    unittest.main()
