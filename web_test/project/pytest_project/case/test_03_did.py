# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: test_03_did.py
@Time: 2019/9/6 23:40
@Desc: Jungle old monster
"""
import pytest
from data.did_data import did_data, assert_suite
from page.did_page import did_page

case_suite = did_data


@pytest.mark.usefixtures("init_did_web")
@pytest.mark.did
class TestDid:
    """
    登录测试用例
    """

    @pytest.mark.parametrize("case_list", case_suite)
    def test_did(self, case_list):

        # 执行投资
        did_page.did(case_list["amount"])

        # 激活did_page自动生成did_page的类属性
        assert_suite()

        # 获取did_data的断言元素的定位
        c: dict = case_list["assert_element"]
        c.items()
        for d in c.values():
            ee = d["element"]

        # 确认当前用例断言元素的定位，执行对应的获取断言方法
        if ee == getattr(did_page, "popup_prompt_element")["element"]:
            actual = did_page.get_popup_prompt_element()
            did_page.click_confirm_popup()
        elif ee == getattr(did_page, "vote_button_element")["element"]:
            actual = did_page.get_vote_button_element()
        elif ee == getattr(did_page, "successful_bidding")["element"]:
            actual = did_page.get_successful_bidding()
            did_page.click_close_success_popup()
        else:
            pass
        expected = case_list["expected"]
        msg = case_list["title"]
        true_result = "pass"
        fail_result = "fail"
        assert expected == actual
        print('{},执行结果为:{}'.format(msg, true_result))


if __name__ == "__main__":
    pytest.main()
