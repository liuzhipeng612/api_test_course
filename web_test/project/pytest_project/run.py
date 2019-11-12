#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Cautious Eureka
@Contact: Eureka@Faisen.com
@Project: cautious_eureka
@File: run.py
@Time: 2019-08-01 23:09
@Desc: Python full stack automation test engineer(Cautious Eureka)
"""
import pytest

if __name__ == "__main__":
    pytest.main(
        [
            "-m login or did",
            "-s",
            "--resultlog=report/test_report.txt",
            "--junitxml=report/test_report.xml",
            "--html=report/test_report.html",
            "--alluredir=report/allure_data/"
        ]
    )
