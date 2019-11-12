# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: test_login.py
@Time: 2019/8/20 21:18
@Desc: Jungle old monster
"""
import unittest
from selenium import webdriver


# 预期结果和实际结果的比较
# if条件
# assert断言
class TestLogin(unittest.TestCase):
    def test_login_error(self):
        """
        测试登录功能异常
        步骤：
        1、启动浏览器，进入登录页面
        2、元素定位用户名和密码
        3、发送用户名和密码（测试数据）
        4、点击登录按钮
        5、断言
        :return:
        """
        driver = webdriver.Chrome()
        login_url = "http://120.78.128.25:8765/Index/login.html"
        driver.get(login_url)
        # 隐式等待
        driver.implicitly_wait(20)

        user_element = driver.find_element_by_name("phone")
        pwd_element = driver.find_element_by_name("password")

        user_element.send_keys("12")
        pwd_element.send_keys("")
        login_button_element = driver.find_element_by_css_selector("button.btn-special")
        # login_button_element.click()
        login_button_element.submit()

        error_msg_element = driver.find_element_by_css_selector("div.form-error-info")
        self.assertEqual(error_msg_element.text, "请输入正确的手机号")


if __name__ == "__main__":
    unittest.main()
