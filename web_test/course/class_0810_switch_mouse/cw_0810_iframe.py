#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0810_iframe.py
@Time: 2019-08-11 01:37
@Desc: Jungle old monster
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# 1、创建WebDriver对象
driver = webdriver.Chrome()

# 2、发起请求
url = 'https://y.qq.com/'
driver.get(url)

# 3、定位元素

# 设置显性等待
wait = WebDriverWait(driver, 1)

###QQ音乐网站，首次进入有时会出现广告弹框，需要判断是否有并关闭，在进行如下操作，这里暂时不做处理。
# 使用显性等待满足条件后执行点击   点击登录按钮激活登录iframe
wait.until(
    EC.presence_of_element_located((By.XPATH, "//a[@class='top_login__link js_login']"))
).click()

# 切换进入iframe
frame_tips = wait.until(
    EC.presence_of_element_located((By.ID, 'frame_tips'))
)
driver.switch_to.frame(frame_tips)

# 如果有第二个iframe（ptlogin_iframe），进入它执行操作  ###QQ音乐这个网站，登录框ptlogin_iframe这个iframe随机出现。
try:
    driver.switch_to.frame('ptlogin_iframe')

except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)

# 如果没有第二个iframe（ptlogin_iframe），抛出异常并继续执行操作
finally:

    # 进入iframe后点击登录
    wait.until(
        EC.presence_of_element_located((By.ID, 'switcher_plogin'))
    ).click()
    time.sleep(1)

    # 切换退出iframe到原先的页面
    driver.switch_to.default_content()

    # 点击关闭弹窗
    wait.until(
        EC.presence_of_element_located((By.XPATH, "//i[@class='popup__icon_close']"))
    ).click()

    # 停留1秒查看执行状况
    time.sleep(1)

    # 关闭浏览器
    driver.close()
