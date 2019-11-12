# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: did_page.py
@Time: 2019/8/27 0:03
@Desc: Jungle old monster
"""
import time
from page.base_page import BasePage
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class DidPage(BasePage):
    """
    登录页面相关定位信息
    """

    # 定位方法+定位元素
    url = "http://120.78.128.25:8765/loan/loan_detail/Id/16343"
    mobile_locator = {"locator": "css", "element": ".form-control.username"}
    password_locator = {"locator": "xpath", "element": "//input[@type='password']"}
    button_locator = {"locator": "css", "element": ".btn.btn-special"}

    invest_unit = {"locator": "css",
                   "element": ".invest-unit.invest-unit-top.mg_top30>.title.tit_style>.float_left.sub_tit_sty"}
    input_box = {"locator": "css", "element": ".form-control.invest-unit-investinput"}
    vote_button = {"locator": "css", "element": ".btn.btn-special.height_style"}
    confirm_popup = {"locator": "css", "element": ".layui-layer-btn0"}
    close_error_popup = {"locator": "css", "element": ".layui-layer-ico.layui-layer-close.layui-layer-close1"}
    close_success_popup = {"locator": "xpath",
                           "element": "//div[@class='layui-layer-content']//div[@class='close_pop']//img"}
    loan_amount = {"locator": "xpath", "element": "//div[@xpath='1']"}

    def open_did_url(self):
        return self.open_url(self.url)

    def mobile_element_clear(self):
        time.sleep(2)
        mobile_locator = self.mobile_locator
        return self.wait_presence_element(mobile_locator["locator"], mobile_locator["element"]).clear()

    def password_element_clear(self):
        time.sleep(2)
        password_locator = self.password_locator
        return self.find_element(password_locator["locator"], password_locator["element"]).clear()

    def input_box_clear(self):
        time.sleep(2)
        input_box = self.input_box
        return self.find_element(input_box["locator"], input_box["element"]).clear()

    def did_login(self, mobile, password):
        """
        登录
        :param mobile: 手机号码
        :param password: 用户密码
        :return: None
        """

        # 打开url
        self.open_did_url()

        # 切换当前窗口
        time.sleep(2)
        self.switch_window()

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

    def did(self, amount):
        input_box = self.input_box
        vote_button = self.vote_button
        invest_unit = self.invest_unit
        invest_unit_element = self.wait_presence_element(invest_unit["locator"], invest_unit["element"])
        self.scroll_to_top(invest_unit_element)
        self.input_box_clear()
        self.wait_presence_element(input_box["locator"], input_box["element"]).send_keys(amount)
        vote_button_element = self.wait_presence_element(vote_button["locator"], vote_button["element"])
        if vote_button_element.text == "投标":
            vote_button_element.click()

    def get_popup_prompt_element(self):
        try:
            popup_prompt_element = getattr(self, "popup_prompt_element")
            return self.wait_visible_element(popup_prompt_element["locator"], popup_prompt_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def get_vote_button_element(self):
        try:
            vote_button_element = getattr(self, "vote_button_element")
            return self.wait_visible_element(vote_button_element["locator"],
                                             vote_button_element["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def get_successful_bidding(self):
        try:
            successful_bidding = getattr(self, "successful_bidding")
            return self.wait_presence_element(successful_bidding["locator"], successful_bidding["element"]).text
        except (TimeoutException, NoSuchElementException) as e:
            print(e)

    def click_confirm_popup(self):
        confirm_popup = self.confirm_popup
        return self.wait_presence_element(confirm_popup["locator"],
                                          confirm_popup["element"]).click()

    def click_close_error_popup(self):
        close_error_popup = self.close_error_popup
        return self.wait_presence_element(close_error_popup["locator"], close_error_popup["element"]).click()

    def click_close_success_popup(self):
        close_success_popup = self.close_success_popup
        return self.wait_presence_element(close_success_popup["locator"], close_success_popup["element"]).click()


did_page = DidPage()
