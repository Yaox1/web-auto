from time import sleep

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.webdriver import WebDriver

from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

driver: WebDriver = webdriver.Chrome()
# 最大化窗口
driver.maximize_window()

# 打开百度首页
driver.get('https://www.baidu.com')

input_element = driver.find_element(By.ID, "kw")
#通过id定位搜索框

input_element.send_keys("周杰伦")
# 模拟点击搜索按钮

driver.find_element(By.ID, "su").click()
#模拟点击搜索按钮
sleep(5)

input_element = driver.find_element(By.ID, "kw")

actions = ActionChains(driver)
actions.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
#全选输入框的内容

# 清空输入框内容
input_element.clear()

driver.find_element(By.ID, "kw").send_keys("李白")
#重新输入李白

driver.find_element(By.ID, "su").click()

sleep(5)
# 关闭浏览器
driver.quit()
