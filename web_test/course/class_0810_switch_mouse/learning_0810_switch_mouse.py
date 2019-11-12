#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0810_switch_mouse.py
@Time: 2019-08-10 09:51
@Desc: Jungle old monster
"""
"""
#iframe标签下面的子页面，是无法定位到的
#先切换到iframe中，之后才能定位
"""
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
url = 'https://ke.qq.com/'
driver.get(url)

# 3、定位元素
try:
    wait = WebDriverWait(driver, 5)
    # 点击登录
    login_element = wait.until(
        EC.presence_of_element_located((By.ID, 'js_login')))
    login_element.click()
    # 点击QQ登录
    login_qq = wait.until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(@class,"btns-enter-qq")]'))
    )
    login_qq.click()

    # 切换到iframe中，然后在定位
    # element = driver.switch_to.active_element
    # alert = driver.switch_to.alert
    # driver.switch_to.default_content()    从iframe中切换到父html页面
    # driver.switch_to.frame('frame_name')  根据iframe标签name属性名来指定
    # driver.switch_to.frame(1) 根据frame的排序值来指定
    # driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0]) 定位的元素对象来定位
    # driver.switch_to.parent_frame()   从iframe中切换到福iframe元素中
    # driver.switch_to.window('main')
    driver.switch_to.frame('login_frame_qq')

    # 点击账号密码登录
    login_iframe = wait.until(
        EC.presence_of_element_located((By.ID, 'switcher_plogin'))
    )
    login_iframe.click()

    # 切换到对应iframe中，然后在定位
    driver.switch_to.default_content()  # 从iframe中切换到父html页面

    # 点击关闭按钮
    close_element = wait.until(
        EC.presence_of_element_located((By.ID, 'login_close'))
    )
    close_element.click()
    time.sleep(10)
except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)
finally:
    driver.quit()
