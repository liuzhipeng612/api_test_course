#!/usr/binW/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: handle_wait.py
@Time: 2019-08-10 17:57
@Desc: Jungle old monster
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1、创建WebDriver对象
browser = webdriver.Chrome()

# 2、发起请求
browser.get('https://www.baidu.com/')  # 打开链接
browser.maximize_window()  # 最大化窗口

# 3、定位元素
# 方法一
# 等待5分钟，如果在10S面之内，都找不到元素，那么抛出异常
# time.sleep(10)
# browser.find_element_by_id("kw").send_keys("柠檬班")

# 方法二
# 显示等待
wait = WebDriverWait(browser, 10)
# until 直到什么为止
# title_is  标题是
# title_contains    标题包含...
# presence_of_element_located   元素出现
# visibility_of_element_located 元素可见
# visibility_of
# presence_of_all_elements_located
# text_to_be_present_in_element
# text_to_be_present_in_element_value
# frame_to_be_available_and_switch_to_it
# invisibility_of_element_located
# element_to_be_clickable
# staleness_of
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selection_state_to_be
# alert_is_present
input_element = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@id='kw']")))
input_element.send_keys("柠檬班")

# 方法三
# 隐式等待
browser.implicitly_wait(10)  # 在使用find_element...定位元素时，会默认等待10s
# 先执行find_element...方法后，如果没有找到元素，执行隐式等待

# 4、关闭会话
browser.close()  # 关闭当前窗口
# browser.quit()  #关闭整个浏览器
