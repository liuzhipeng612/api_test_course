# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: test_02_login.py
@Time: 2019/8/27 0:25
@Desc: Jungle old monster
"""
import unittest
from library.ddt import ddt, data
from data.login_data import login_data, assert_suite
from page.login_page import LoginPage

case_suite = login_data


@ddt
class TestLogin(unittest.TestCase):
    """
    登录测试用例
    """
    login_page = LoginPage()

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.login_page.quit()

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @data(*case_suite)
    def test_login(self, case_list):
        login_page = self.login_page

        # 登录
        login_page.login(case_list["mobile"], case_list["password"])

        # 激活login_page自动生成login_page的类属性
        assert_suite()

        # 获取login_data的断言元素的定位
        c: dict = case_list["assert_element"]
        c.items()
        for d in c.values():
            ee = d["element"]

        # 确认当前用例断言元素的定位，执行对应的获取断言方法
        if ee == getattr(login_page, "mobile_error_element")["element"]:
            actual = login_page.get_mobile_error_element()
        elif ee == getattr(login_page, "user_name_element")["element"]:
            actual = login_page.get_user_name_element()
            login_page.logout()
        elif ee == getattr(login_page, "password_error_element")["element"]:
            actual = login_page.get_password_error_element()
        elif ee == getattr(login_page, "mobile_password_error_element")["element"]:
            actual = login_page.get_mobile_password_error_element()
        else:
            pass
        expected = case_list["expected"]
        msg = case_list["title"]
        true_result = "pass"
        fail_result = "fail"
        try:
            self.assertEqual(expected, actual, msg)
            print('{},执行结果为:{}'.format(msg, true_result))
        except AssertionError as e:
            print("{}, 执行结果为: {},具体异常为{}".format(msg, fail_result, e))


if __name__ == "__main__":
    unittest.main()
