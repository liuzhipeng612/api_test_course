# !/USR/BIN/ENV PYTHON
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: did_data.py.py
@Time: 2019/8/24 10:21
@Desc: Jungle old monster
"""
from page.did_page import DidPage

"""
投资测试的数据
"""

login_data = {"title": "已注册的手机号码", "mobile": "17322322629", "password": "q1234567890", "expected": "我的帐户[小小鸟]",
              "assert_element": {
                  "user_name_element": {"locator": "xpath", "element": "//img[@class='mr-5']/parent::a"}}}

did_data = [
    {"title": "输入0进行投标", "amount": "0", "expected": "请正确填写投标金额",
     "assert_element": {
         "popup_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}},
    {"title": "输入非10整数倍非100整数倍", "amount": "11", "expected": "请输入10的整数倍",
     "assert_element": {"vote_button_element": {"locator": "css", "element": ".btn.btn-special.height_style"}}},
    {"title": "输入10进行投标", "amount": "10", "expected": "投标金额必须为100的倍数",
     "assert_element": {
         "bullet_box_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}},
    {"title": "输入10的整数倍非100整数倍", "amount": "1010", "expected": "投标金额必须为100的倍数",
     "assert_element": {
         "bullet_box_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}},
    {"title": "输入100进行投标", "amount": "100", "expected": "投标成功！",
     "assert_element": {"successful_bidding": {"locator": "xpath",
                                               "element": "//div[@class='layui-layer-content']"
                                                          "//div[@class='capital_font1 note']"}}},
    {"title": "输入负数进行投标", "amount": "-100", "expected": "请正确填写投标金额",
     "assert_element": {
         "bullet_box_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}},
    {"title": "输入小数进行投标", "amount": "100.000", "expected": "投标成功！",
     "assert_element": {"successful_bidding": {"locator": "xpath",
                                               "element": "//div[@class='layui-layer-content']"
                                                          "//div[@class='capital_font1 note']"}}},
    {"title": "输入非数字进行投标", "amount": "abc", "expected": "请输入10的整数倍",
     "assert_element": {"vote_button_element": {"locator": "css", "element": ".btn.btn-special.height_style"}}},
    {"title": "输入小于余额的金额投标", "amount": "100", "expected": "投标成功！",
     "assert_element": {"successful_bidding": {"locator": "xpath",
                                               "element": "//div[@class='layui-layer-content']"
                                                          "//div[@class='capital_font1 note']"}}},
    {"title": "输入大于余额的金额投标", "amount": "1234567890987654321", "expected": "投标金额大于可用金额",
     "assert_element": {
         "bullet_box_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}},
    {"title": "输入大于借款金额的金额投标", "amount": "1234567890987654321", "expected": "购买标的金额不能大于标总金额",
     "assert_element": {
         "bullet_box_prompt_element": {"locator": "css", "element": ".layui-layer-content>.text-center"}}}
]


def assert_suite():
    assert_list = []
    for i in did_data:
        j = i["assert_element"]
        k = j.items()
        for l in k:
            if l not in assert_list:
                assert_list.append(l)
    for m in assert_list:
        n = m[0]
        o = m[1]
        setattr(DidPage, n, o)

    # print(assert_list)


dd = assert_suite()
pass
