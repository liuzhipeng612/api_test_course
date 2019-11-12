#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0725_mock_webservice.py
@Time: 2019-08-07 00:48
@Desc: Eureka
"""
from unittest import mock
import requests


def request_lemfix():
    return requests.get('http://www.lemfix.com/').text


def print_content():
    print(request_lemfix())


if __name__ == "__main__":
    request_lemfix = mock.Mock(return_value="这里会显示柠檬班论坛内容")
    print_content()
