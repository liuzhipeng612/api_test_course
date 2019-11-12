#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0810_alert.py
@Time: 2019-08-11 17:10
@Desc: Jungle old monster
"""
# 出现alert弹窗，其他元素就不能被定位到，只能定位alert的弹窗
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 1、创建WebDriver对象
driver = webdriver.Chrome()

# 2、发起请求
file_path = 'file:///' + os.path.abspath('../class_0803_dom_xpath/index.html')
url = file_path
driver.get(url)

# 3、定位元素
try:
    wait = WebDriverWait(driver, 5)
    wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'h1'))).click()
    time.sleep(5)
    # 方法一
    # driver.switch_to.alert.dismiss()  # 点击取消
    # driver.switch_to.alert.accept()  # 点击确定
    # driver.switch_to.alert.send_keys()  # 输入内容

    # 方法二
    wait.until(
        EC.alert_is_present()).accept()
    content_element = driver.find_element_by_xpath('//div[@class="content"]/div')
    print(content_element.get_attribute('class'))
    time.sleep(10)
except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)
finally:
    driver.quit()
