# !/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0813_select_window.py
@Time: 2019/8/19 23:47
@Desc: Jungle old monster
"""
# import keyring
import re
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from handle_config import do_config
from handle_path import CONFIG_GREETINGS_FILE_PATH

# 初始化Chrome对象
driver = webdriver.Chrome()

# 定义url
url = "http://www.lemfix.com/nmb_musen"

# 打开url
driver.get(url)

# 最大化窗口
driver.maximize_window()

try:
    # 等待
    driver.implicitly_wait(2)
    wait = WebDriverWait(driver, 3)
    # 切换新窗口
    now_handle = driver.current_window_handle


    def switch_window(drivers, now_handles):
        all_handles = driver.window_handles  # 得到当前开启的所有窗口的句柄
        for handle in all_handles:
            if handle != now_handles:  # 获取到与当前窗口不一样的窗口
                drivers.switch_to_window(handle)


    # 登录
    login = driver.find_element(By.XPATH, "//a[@href='/account/sign_in']")
    login.click()

    # 切换窗口
    switch_window(driver, now_handle)

    user_name = wait.until(
        EC.presence_of_element_located((By.XPATH, "//input[@id='user_login']"))
    )
    # user_name = driver.find_element(By.XPATH, "//input[@id='user_login']")
    user_name.send_keys("jomer3126")
    password = driver.find_element(By.XPATH, "//input[@id='user_password']")
    password.send_keys("1234567890")
    commit = driver.find_element(By.XPATH, "//input[@name='commit']")
    commit.click()

    # 切换窗口
    switch_window(driver, now_handle)

    # 进入可优博客
    keyou_blog = wait.until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='topic media topic-355']//img"))
    )
    keyou_blog.click()

    # 切换窗口
    switch_window(driver, now_handle)

    # 定位列表所有url
    a_title_element = wait.until(
        EC.presence_of_all_elements_located((By.XPATH, "//div[@class='title']/a[@title]"))
    )
    # a_title_element = driver.find_elements(By.XPATH, "//div[@class='title']/a[@title]")

    # 搜集所有文章标题和url
    href_list = []
    title_list = []
    for i in a_title_element:
        href_value = i.get_attribute("href")
        title_value = i.get_attribute("title")
        href_list.append(href_value)
        title_list.append(title_value)
    print(href_list)

    # 依次打开列表url并执行操作
    k = 0
    for j in href_list:
        driver.get(j)
        like = driver.find_element(By.XPATH, "//div[@class='opts']//a[1]")
        like.click()
        textarea = driver.find_element(By.XPATH, "//textarea[@id='reply_body']")
        k += 1
        textarea_content = do_config.get_value("Greetings", str(k))
        text_random = str(random.randint(1000, 9999))
        textarea.send_keys(textarea_content + text_random)
        button = driver.find_element(By.XPATH, "//button[@id='reply-button']")
        button.click()
        article_title = driver.find_element(By.XPATH, "//h1[@class='media-heading']/span[@class='title']").text
        driver.save_screenshot(article_title + ".png")
except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)
finally:
    # 关闭页面
    driver.quit()
