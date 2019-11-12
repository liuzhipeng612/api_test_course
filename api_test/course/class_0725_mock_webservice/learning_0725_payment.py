#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0725_payment.py
@Time: 2019-08-07 01:00
@Desc: Eureka
"""
import requests


class Payment:
    """
    定义第三方支付类
    """

    def auth(self, card_num, amount):
        """
        请求第三方外部支付接口的方法，返回响应状态码
        :param card_num:卡号
        :param amount:金额
        :return:返回状态码，200代表支付成功，500代表支付异常，失败
        """
        url = "http://第三方支付url.payment"
        data = {"card_num": card_num, "amount": amount}  # 请求参数
        self.res = requests.post(url, data=data)
        return self.res.status_code  # 返回的状态码

    def pay(self, user_id, card_num, amount):
        """

        :param user_id:
        :param card_num:
        :param amount:
        :return:
        """
        try:
            status_code = self.auth(card_num, amount)
        except TimeoutError:
            status_code = self.auth(card_num, amount)  # 如果支付超时，再请求一次
        if status_code == 200:
            print("[{}]支付[{}]成功！！！进行扣款并登记支付记录".format(user_id, amount))
            return "success"
        elif status_code == 500:
            print("[{}]支付[{}]失败！！！不进行扣款".format(user_id, amount))
            return "Fail"
