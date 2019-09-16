from selenium import  webdriver

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome(r'E:\webdriver\chromedriver.exe')
browser.maximize_window()
browser.get('http://www.uestc.edu.cn/')
# 方法一：使用find_element_by_link_text找到顶级菜单，并将鼠标移动到上面
article = browser.find_element_by_link_text(u'学校概况')
ActionChains(browser).move_to_element(article).perform()
# 方法二：使用find_element_by_xpath找到顶级菜单，并将鼠标移动到上面
# article = browser.find_element_by_xpath('//a[contains(@href,"?ch/3")]')
# ActionChains(browser).move_to_element(article).perform()
# 方法一：使用find_element_by_link_text找到二级菜单，并点击
# menu = browser.find_element_by_link_text(u'学校简介')
# 方法二：使用find_element_by_xpath找到二级菜单，并点击
menu = browser.find_element_by_xpath('//li[@classes="first odd nth1"]')
# menu.click()
