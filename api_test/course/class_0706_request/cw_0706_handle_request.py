#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0706_handle_request.py
@Time: 2019-07-08 22:21
@Desc: Jungle old monster
"""
from interface_automation.class_0706_request.cw_0706_request import do_request


class HandleRequest:
    def __init__(self):
        pass

    def get_register(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    def post_register(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    def get_login(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    def post_login(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    def get_recharge(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    def post_recharge(self, method, url, params):
        res = do_request.send_request(method=method, url=url, data=params)

    pass


if __name__ == '__main__':
    # 使用get方法请求注册接口
    get_register_method = 'GET'
    get_register_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
    get_register_params = {'mobilephone': 13798288888, 'pwd': 123456, 'regname': '刀刀'}
    my_get_register = HandleRequest()
    my_get_register.get_register(get_register_method, get_register_url, get_register_params)
    # 使用post方法请求注册接口
    post_register_method = 'POST'
    post_register_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/register'
    post_register_params = {'mobilephone': 13798288888, 'pwd': 123456, 'regname': '刀刀'}
    my_post_register = HandleRequest()
    my_post_register.post_register(post_register_method, post_register_url, post_register_params)

    # 使用get方法请求登录接口
    get_login_method = 'GET'
    get_login_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/login'
    get_login_params = {'mobilephone': 13798288888, 'pwd': 123456}
    my_get_login = HandleRequest()
    my_get_login.get_login(get_login_method, get_login_url, get_login_params)
    # 使用post方法请求登录接口
    post_login_method = 'POST'
    post_login_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/login'
    post_login_params = {'mobilephone': 13798288888, 'pwd': 123456}
    my_post_login = HandleRequest()
    my_post_login.post_login(post_login_method, post_login_url, post_login_params)

    # 使用get方法请求充值接口
    get_recharge_method = 'GET'
    get_recharge_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge'
    get_recharge_params = {'mobilephone': 13798288888, 'amount': 123456}
    my_get_recharge = HandleRequest()
    my_get_recharge.get_recharge(get_recharge_method, get_recharge_url, get_recharge_params)
    # 使用post方法请求充值接口
    post_recharge_method = 'POST'
    post_recharge_url = 'http://test.lemonban.com:8080/futureloan/mvc/api/member/recharge'
    post_recharge_params = {'mobilephone': 13798288888, 'amount': 123456}
    my_post_recharge = HandleRequest()
    my_post_recharge.post_recharge(post_recharge_method, post_recharge_url, post_recharge_params)
