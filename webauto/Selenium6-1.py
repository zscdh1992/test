from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import  time

hw_menulist = ['智能手机','笔记本','平板','智能穿戴','智能家居','更多产品','软件应用','服务与支持']
shop_menuslist = ['平板电脑','笔记本电脑','笔记本配件',]

driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get('https://www.vmall.com/')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@href="http://consumer.huawei.com/cn/"]').click()
time.sleep(1)
shop_handle = driver.current_window_handle
handles = driver.window_handles
for handle in handles:
    if handle != driver.current_window_handle:
        driver.switch_to.window(handle)
        print('------切换至华为页面------')

hw_menus = driver.find_elements_by_xpath('//*[@class="clearfix nav-cnt"]/li')
for hw_menu in hw_menus:
    if hw_menu.text.strip() in hw_menulist:
        print(hw_menu.text.strip(),'pass!')
    else:
        print(hw_menu.text.strip(), 'failed!')


print('------切换至商城页面------')
driver.switch_to.window(shop_handle)
article = driver.find_element_by_link_text(u'笔记本 & 平板')
ActionChains(driver).move_to_element(article).perform()


shop_menus = driver.find_elements_by_xpath('//*[@id ="zxnav_1"]//ul/li[position()<last()]')
for shop_menu in shop_menus:
    if shop_menu.text.strip() in shop_menuslist:
        print(shop_menu.text.strip(),'pass!')
    else:
        print(shop_menu.text.strip(), 'failed!')


driver.quit()