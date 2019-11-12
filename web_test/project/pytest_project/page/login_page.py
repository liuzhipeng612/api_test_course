# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: login_page.py
@Time: 2019/8/27 0:01
@Desc: Jungle old monster
"""
import time
from page.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage(BasePage):
    """
    登录页面相关定位信息
    """

    # 定位方法+定位元素
    url = "http://120.78.128.25:8765/Index/login.html"
    mobile_locator = {"locator": "css", "element": ".form-control.username"}
    password_locator = {"locator": "xpath", "element": "//input[@type='password']"}
    button_locator = {"locator": "css", "element": ".btn.btn-special"}
    user_logout = {"locator": "xpath", "element": "//div[@class='right fs-12']/span[last()]/a"}

    # user_name_element = {"locator": "xpath", "element": "//img[@class='mr-5']/parent::a"}
    # mobile_password_error_element = {"locator": "css", "element": ".layui-layer-content"}
    # mobile_error_element = {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}
    # password_error_element = {"locator": "xpath", "element": "//input[@name='password']/following-sibling::div"}

    def open_login_url(self):
        return self.open_url(self.url)

    def logout(self):
        user_logout = self.user_logout
        return self.wait_visible_element(user_logout["locator"], user_logout["element"]).click()

    def mobile_element_clear(self):
        time.sleep(2)
        mobile_locator = self.mobile_locator
        return self.wait_presence_element(mobile_locator["locator"], mobile_locator["element"]).clear()

    def password_element_clear(self):
        time.sleep(2)
        password_locator = self.password_locator
        return self.find_element(password_locator["locator"], password_locator["element"]).clear()

    def login(self, mobile, password):
        """
        登录
        :param mobile: 手机号码
        :param password: 用户密码
        :return: None
        """

        # 打开url
        self.open_login_url()

        # 最大化窗口
        self.maximize_window()

        # 清空用户名和密码
        self.mobile_element_clear()
        self.password_element_clear()

        # 定位登录元素点击登录
        mobile_locator = self.mobile_locator
        self.wait_presence_element(mobile_locator["locator"], mobile_locator["element"]).send_keys(mobile)
        password_locator = self.password_locator
        self.find_element(password_locator["locator"], password_locator["element"]).send_keys(password)
        button_locator = self.button_locator
        self.find_element(button_locator["locator"], button_locator["element"]).click()

    def get_user_name_element(self):
        """
        成功登陆
        :return: 用户名
        """
        # 切换窗口
        self.switch_window()

        # 获取可见用户名
        try:
            user_name_element = getattr(self, "user_name_element")
            return self.wait_visible_element(user_name_element["locator"], user_name_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def get_mobile_password_error_element(self):
        """

        :return:
        """
        try:
            mobile_password_error_element = getattr(self, "mobile_password_error_element")
            return self.wait_visible_element(mobile_password_error_element["locator"],
                                             mobile_password_error_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def get_mobile_error_element(self):
        try:
            mobile_error_element = getattr(self, "mobile_error_element")
            return self.wait_visible_element(mobile_error_element["locator"], mobile_error_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def get_password_error_element(self):
        try:
            password_error_element = getattr(self, "password_error_element")
            return self.wait_visible_element(password_error_element["locator"], password_error_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)


login_page = LoginPage()
