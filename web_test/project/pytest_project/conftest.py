# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: pytest_project
@File: conftest.py
@Time: 2019/9/15 11:28
@Desc: Jungle old monster
"""
import pytest
from data.did_data import login_data
from page.login_page import login_page
from page.did_page import did_page


@pytest.fixture(scope="class")
def init_login_web():
    yield
    login_page.quit()


@pytest.fixture(scope="class")
def init_did_web():
    did_page.did_login(login_data["mobile"], login_data["password"])
    yield
    did_page.quit()
