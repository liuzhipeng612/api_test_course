# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: login_data.py
@Time: 2019/8/24 10:22
@Desc: Jungle old monster
"""
from page.login_page import LoginPage

"""
登录测试的数据
"""
# login_data = [{"title": "不满足11位的数字", "mobile": "1868472055", "password": "python",
#                "expected": "请输入正确的手机号",
#                "assert_element": {
#                    "mobile_error_element": {"locator": "xpath",
#                                             "element": "//input[@name='phone']/following-sibling::div"}}}, ]


login_data = [
    {"title": "已注册的手机号码", "mobile": "18684720553", "password": "python", "expected": "我的帐户[小小鸟]",
     "assert_element": {"user_name_element": {"locator": "xpath", "element": "//img[@class='mr-5']/parent::a"}}},
    {"title": "未注册的手机号码", "mobile": "17322322628", "password": "python",
     "expected": "此账号没有经过授权，请联系管理员!",
     "assert_element": {"mobile_password_error_element": {"locator": "css", "element": ".layui-layer-content"}}},
    {"title": "手机号码为空", "mobile": "", "password": "q1234567890", "expected": "请输入手机号",
     "assert_element": {
         "mobile_error_element": {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}}},
    {"title": "不满足11位的数字", "mobile": "1868472055", "password": "python",
     "expected": "请输入正确的手机号",
     "assert_element": {
         "mobile_error_element": {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}}},
    {"title": "满足11位的非手机号码数字", "mobile": "11684720553", "password": "python",
     "expected": "请输入正确的手机号",
     "assert_element": {
         "mobile_error_element": {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}}},
    {"title": "超过11位的手机号码", "mobile": "186847205532", "password": "python",
     "expected": "请输入正确的手机号",
     "assert_element": {
         "mobile_error_element": {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}}},
    {"title": "手机号码填写非数字", "mobile": "askjadslkdj", "password": "python",
     "expected": "请输入正确的手机号",
     "assert_element": {
         "mobile_error_element": {"locator": "xpath", "element": "//input[@name='phone']/following-sibling::div"}}},
    {"title": "与手机号匹配的密码登录", "mobile": "18684720553", "password": "python",
     "expected": "我的帐户[小小鸟]",
     "assert_element": {"user_name_element": {"locator": "xpath", "element": "//img[@class='mr-5']/parent::a"}}},
    {"title": "与手机号不匹配的密码登录", "mobile": "18684720553", "password": "python123",
     "expected": "帐号或密码错误!",
     "assert_element": {"mobile_password_error_element": {"locator": "css", "element": ".layui-layer-content"}}},
    {"title": "密码为空", "mobile": "18684720553", "password": "", "expected": "请输入密码",
     "assert_element": {
         "password_error_element": {"locator": "xpath", "element": "//input[@name='password']/following-sibling::div"}}}
]


def assert_suite():
    assert_list = []
    for i in login_data:
        j = i["assert_element"]
        k = j.items()
        for l in k:
            if l not in assert_list:
                assert_list.append(l)
    for m in assert_list:
        n = m[0]
        o = m[1]
        setattr(LoginPage, n, o)
