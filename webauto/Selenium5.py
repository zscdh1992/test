from selenium import  webdriver
from selenium.webdriver.support.ui import Select
import  time

driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.get('https://kyfw.12306.cn/otn/leftTicket/init')
driver.implicitly_wait(10)

#输入出发地
fromStation = driver.find_element_by_xpath('//*[@id="fromStationText"]')
fromStation.click()
fromStation.send_keys('南京南\n')

#输入目的地
toStation = driver.find_element_by_xpath('//*[@id="toStationText"]')
toStation.click()
toStation.send_keys('杭州东\n')

#选择发车时间
cc_start_time = Select(driver.find_element_by_xpath('//*[@id="cc_start_time"]'))
cc_start_time.select_by_visible_text("00:00--06:00")

#点击查询并切换到第二天
driver.find_element_by_xpath('//*[@id="query_ticket"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="sear-sel"]/div/ul/li[2]').click()

#判断二等座有票的车次，打印车次
driver.implicitly_wait(10)
time.sleep(1)
tickets = driver.find_elements_by_xpath('//*[@id="queryLeftTable"]/tr[contains(@id,"ticket")]')
for ticket in tickets:
    has_tickets = ticket.find_element_by_xpath('.//td[4]').text #获取当前车次二等座的余票情况
    if has_tickets =='--' or has_tickets =='无'  or has_tickets =='候补': #判断无票，则查询下一班次
        continue
    else: #判断有票，则打印车次
        train_number = ticket.find_element_by_xpath('.//div[@class="train"]/div').text
        print(train_number)


driver.quit()