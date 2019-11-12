import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
file_path = 'file:///' + os.path.abspath('../class_0803_dom_xpath/index.html')
url = file_path
driver.get(url)

try:
    wait = WebDriverWait(driver, 1)
    wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1'))).click()
    time.sleep(1)
    wait.until(EC.alert_is_present()).dismiss()
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH,
             "//input[@placeholder='请输入姓名']"))).send_keys("树树", Keys.RETURN)
    time.sleep(1)
except (TimeoutException, NoSuchElementException) as e:
    print("出现异常：", e)
finally:
    driver.quit()
