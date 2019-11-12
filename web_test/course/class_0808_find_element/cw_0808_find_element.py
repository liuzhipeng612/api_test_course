#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: Jomer
@File: cw_0808_find_element.py
@Time: 2019-08-10 21:18
@Desc: Jungle old monster
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1、创建WebDriver对象
driver = webdriver.Chrome()

# 2、发起请求
url = 'https://www.baidu.com/'
driver.get(url)

##### 1.演练selenium中查找元素的相关方法

# 3、定位元素
# find_element_by_id    通过di进行定位元素
# driver.find_element_by_id('kw').send_keys('菜菜', Keys.RETURN)
# driver.find_element(By.ID, 'kw').send_keys('菜菜', Keys.RETURN)

# find_element_by_name  通过name进行定位
# driver.find_element_by_name('wd').send_keys('菜菜', Keys.RETURN)
# driver.find_element(By.NAME,'wd').send_keys('菜菜', Keys.RETURN)

# find_element_by_xpath 通过xpath进行定位
# driver.find_element_by_xpath("//input[@id='kw']").send_keys('菜菜', Keys.RETURN)
# driver.find_element(By.XPATH,"//input[@id='kw']").send_keys('菜菜', Keys.RETURN)

# find_element_by_link_text 通过a标签的文本进行定位
# driver.find_element_by_link_text('新闻').click()
# driver.find_element(By.LINK_TEXT,'新闻').click()

# find_element_by_partial_link_text 通过a标签的部分文本进行定位
# driver.find_element_by_partial_link_text('新').click()
# driver.find_element(By.PARTIAL_LINK_TEXT,'新').click()

# find_element_by_tag_name  通过标签名称进行定位
# driver.find_element_by_tag_name('title')
# driver.find_element(By.TAG_NAME,'title')

# find_element_by_class_name    通过类名进行定位
# driver.find_element_by_class_name('s_ipt').send_keys('菜菜', Keys.RETURN)
# driver.find_element(By.CLASS_NAME,'s_ipt').send_keys('菜菜', Keys.RETURN)

# find_element_by_css_selector  通过css选择器进行定位
# driver.find_element_by_css_selector('#kw').send_keys('菜菜', Keys.RETURN)
# driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('菜菜', Keys.RETURN)

##### 2.演练selenium中的三种等待的相关操作
# 方法一
# by_id = driver.find_element(By.ID, 'kw')
# time.sleep(10)
# by_id.send_keys('菜菜', Keys.RETURN)
# time.sleep(10)

# 4、关闭会话
# driver.close()

# 方法二
# try:
#     element = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, 'kw'))
#     )
#     element.send_keys('菜菜', Keys.RETURN)
#     time.sleep(10)
# finally:
#     driver.quit()

# 方法三   环境限定为执行任意操作，时间超过5s
driver.implicitly_wait(10)
try:
    driver.find_element_by_xpath("//div[@id='u1']//a[@name='tj_login']").click()
    driver.find_element_by_xpath("//p[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
    time.sleep(10)
finally:
    driver.quit()
