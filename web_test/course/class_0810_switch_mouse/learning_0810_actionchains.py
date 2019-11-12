#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: learning_0810_actionchains.py
@Time: 2019-08-11 23:25
@Desc: Jungle old monster
"""
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains

# 1、创建WebDriver对象
driver = webdriver.Chrome()

# 2、发起请求
url = 'https://www.baidu.com/'
driver.get(url)

# 3、定位元素
try:
    wait = WebDriverWait(driver, 5)
    setup_element = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='u1']//a[@name='tj_settingicon']"))
    )
    # 初始化ActionChains实例对象
    action_chains = ActionChains(driver)
    # 设置ActionChains动作
    # action_chains.drag_and_drop() 有较多Bug，建议不使用
    # action_chains.click_and_hold().move_to_element().release().perform() 点击目标并拖动目标，将目标移动到目的地，松开鼠标，执行操作
    action_chains.move_to_element(setup_element)
    # 执行动作
    action_chains.perform()

    # 点击高级搜索
    wait.until(
        EC.presence_of_element_located((By.XPATH, '//div[@class="bdpfmenu"]/a[2]'))
    ).click()
    time.sleep(10)
except (TimeoutException, NoSuchElementException) as e:
    print(e)
finally:
    driver.quit()
