#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: handle_browser.py
@Time: 2019-08-10 00:32
@Desc: Jungle old monster
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# 1、创建WebDriver对象
browser = webdriver.Chrome()

# 2、发起请求
browser.get('https://www.baidu.com/')  # 打开链接
browser.maximize_window()  # 最大化窗口

# 3定位元素
# 使用单个值进行定位
# find_element_by_id    通过ID值进行定位
# find_element_by_name  多个name时获取第一个name
# find_element_by_xpath 使用xpath定位
# find_element_by_link_text 通过a标签的文本定位
# find_element_by_partial_link_text 通过a标签的部分文本定位
# find_element_by_tag_name 使用标签名字来定位，多个时取第一个
# find_element_by_class_name 使用类名进行定位
# find_element_by_css_selector 通过css选择器定位

# 通过多个值进行定位
# find_elements_by_name
# find_elements_by_xpath
# find_elements_by_link_text
# find_elements_by_partial_link_text
# find_elements_by_tag_name
# find_elements_by_class_name
# find_elements_by_css_selector

# 开后门/走捷径的方法 -->万祖归宗
# find_element
# find_elements

##举例
# input_element = browser.find_element_by_id("kw")
# input_element = browser.find_element_by_name("wd")
# input_element = browser.find_element_by_xpath("//input[@id='kw']")
# browser.find_element_by_link_text("新闻").click()
# browser.find_element_by_partial_link_text("新").click()
# input_element = browser.find_element_by_css_selector("#kw")
input_element = browser.find_element(By.ID, "kw")
input_element.send_keys("柠檬班")

# 4、操作
# 点击、输入、拖拽、下拉


# 5、关闭会话
browser.close()  # 关闭当前窗口
# browser.quit()  #关闭整个浏览器
