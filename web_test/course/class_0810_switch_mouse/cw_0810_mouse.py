#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0810_mouse.py
@Time: 2019-08-12 00:28
@Desc: Jungle old monster
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
url = 'https://www.baidu.com/'
driver.get(url)

try:
    wait = WebDriverWait(driver, 2)

    # 定位设置按钮
    settings_button = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@id='u1']/a[last()-1]"))
    )

    # 创建鼠标对象
    action_chains = ActionChains(driver)

    # 移动鼠标到设置按钮
    action_chains.move_to_element(settings_button)

    # 执行鼠标操作
    action_chains.perform()

    # 定位高级搜索并点击
    advanced_search = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='bdpfmenu']/a[2]"))
    ).click()

    # 输入文本 树树
    wait.until(
        EC.presence_of_element_located((By.ID, 'adv_keyword'))
    ).send_keys("树树")

    # 定位搜索时间下拉框并点击
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='gpc']"))
    ).click()

    # 定位年选项
    year_option = wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='gpc']"))
    )

    # 调用select选择年选项
    select = Select(year_option)
    time.sleep(1)
    select.select_by_index(4)

    # 定位文档格式并点击
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='ft']"))
    ).click()

    # 定位所有格式
    all_formats = wait.until(
        EC.presence_of_element_located((By.XPATH, "//select[@name='ft']"))
    )

    # 调用select选择所有格式
    select = Select(all_formats)
    time.sleep(1)
    select.select_by_index(6)
    time.sleep(1)

    # 定位高级搜索并点击
    search = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@class='advanced-search-btn']"))
    ).click()
    time.sleep(2)

    # 切换新窗口
    now_handle = driver.current_window_handle


    def switch_window(driver, now_handle):
        all_handles = driver.window_handles  # 得到当前开启的所有窗口的句柄
        for handle in all_handles:
            if handle != now_handle:  # 获取到与当前窗口不一样的窗口
                driver.switch_to_window(handle)


    switch_window(driver, now_handle)

    # 执行界面快照
    driver.save_screenshot('screenshot.png')
    time.sleep(2)
except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)
finally:
    driver.quit()
