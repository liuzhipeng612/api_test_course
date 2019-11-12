#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0725_test_pay.py
@Time: 2019-08-07 01:17
@Desc: Eureka
"""
import unittest
from unittest import mock
from .learning_0725_payment import Payment


class PaymentTest(unittest.TestCase):
    """
    测试支付接口
    """

    def setUp(self):
        self.payment = Payment()

    def test_01_success(self):
        """
        测试支付成功
        :return:
        """
        self.payment.auth = mock.Mock(return_value=200)
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("success", res)

    def test_02_fail(self):
        """
                测试支付失败
                :return:
                """
        self.payment.auth = mock.Mock(return_value=500)
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("Fail", res)

    def test_03_retry_success(self):
        """
        测试调用第三方接口超时之后，再次支付成功
        :return:
        """
        self.payment.auth = mock.Mock(side_effect=[TimeoutError, 200])
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("success", res)

    def test_04_retry_ail(self):
        """
        测试调用第三方接口超时之后，再次支付失败
        :return:
        """
        self.payment.auth = mock.Mock(side_effect=[TimeoutError, 500])
        res = self.payment.pay(user_id=1001, card_num=12345, amount=500000)
        self.assertEqual("Fail", res)


if __name__ == "__main__":
    unittest.main()
