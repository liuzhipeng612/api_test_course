#!/usr/bin/env python
# coding=UTF-8
"""
@Author: Jomer
@Contact: jomer3126@gmail.com
@Project: unittest_project
@File: base_page.py
@Time: 2019/8/29 12:58 下午
@Desc: Jungle old monster
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    selenium封装
    """

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.By = By

    # 打开url
    def open_url(self, url):
        return self.driver.get(url)

    def quit(self):
        return self.driver.quit()

    def close(self):
        return self.driver.close()

    # 最大化窗口
    def maximize_window(self):
        time.sleep(2)
        return self.driver.maximize_window()

    # 窗口切换
    def now_handle(self):
        """
        获取当前窗口
        :return: 当前窗口句柄
        """
        return self.driver.current_window_handle

    def switch_window(self):
        """
        切换新窗口
        :return: 新窗口句柄
        """
        driver = self.driver
        now_handle = self.now_handle
        for handle in driver.window_handles:  # 遍历所有窗口
            if handle != now_handle:  # 获取到与当前窗口不一样的窗口
                return driver.switch_to_window(handle)

    # 等待
    def implicitly_wait(self):
        """
        隐式等待
        :return: 隐式等待20秒
        """
        return self.driver.implicitly_wait(20)

    def wait(self):
        """
        显示等待
        :return: 显示等待5秒
        """
        return WebDriverWait(self.driver, 5)

    # 元素定位方法By.XXX
    def by_locator(self, locator):
        if locator == "css":
            return self.By.CSS_SELECTOR
        elif locator == "class_name":
            return self.By.CLASS_NAME
        elif locator == "id":
            return self.By.ID
        elif locator == "name":
            return self.By.NAME
        elif locator == "partial_link_text":
            return self.By.PARTIAL_LINK_TEXT
        elif locator == "tag_name":
            return self.By.TAG_NAME
        elif locator == "xpath":
            return self.By.XPATH
        else:
            return None

    # 定位元素
    def find_element(self, locator, element) -> WebElement:
        return self.driver.find_element(self.by_locator(locator), element)

    # 等待定位元素
    def wait_presence_element(self, locator, element) -> WebElement:
        """
        等待元素出现/存在
        :param locator: 定位方法
        :param element: 定位元素
        :return: 被定位的元素对象
        """
        try:
            return self.wait().until(
                EC.presence_of_element_located((self.by_locator(locator), element))
            )
        except Exception as e:
            print(e)
        finally:
            pass

    def wait_visible_element(self, locator, element) -> WebElement:
        """
        等待元素可见->视觉可见
        :param locator: 定位方法
        :param element: 定位元素
        :return: 被定位的元素对象
        """
        try:
            return self.wait().until(
                EC.visibility_of_element_located((self.by_locator(locator), element))
            )
        except Exception as e:
            print(e)
        finally:
            pass

    def wait_click_element(self, locator, element) -> WebElement:
        """
        返回一个WebElement对象，如果没有找到就报错
        :param locator: 定位方法
        :param element: 定位元素
        :return: 被定位的元素对象
        """
        try:
            return self.wait().until(
                EC.element_to_be_clickable((self.by_locator(locator), element))
            )
        except Exception as e:
            print(e)
        finally:
            pass

    # 切换iframe
    # 切换弹窗
    def scroll_to_top(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView()", element)

    def scroll_to_center(self, element):
        return self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'center'})", element)

    def scroll_to_bottom(self, element):
        return self.driver.execute_script("arguments[0].scrollIntoView(false)", element)
# 鼠标操作
# 单击
# 双击
# 右击
# 滚动窗口
# 键盘操作
# 上传文件
