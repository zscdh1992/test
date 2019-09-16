from selenium import  webdriver
import  time
driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.get('http://www.51job.com')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@class="more"]').click()
driver.implicitly_wait(10)

input1 = driver.find_element_by_id('kwdselectid')

input1.send_keys('python')

driver.find_element_by_xpath('//*[@id="work_position_input"]').click()
selected_citys = driver.find_elements_by_xpath('//*[@id="work_position_click_multiple_selected"]/span')
time.sleep(1)
for  city  in selected_citys:
    city.click()

driver.find_element_by_xpath('//*[@id="work_position_click_center_right_list_category_000000_080200"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="work_position_click_bottom_save"]').click()
time.sleep(1)

driver.find_element_by_xpath('//*[@class="c c_h c_bd"]/label[1]').click()
driver.find_element_by_xpath('//*[@id="funtype_click"]').click()
driver.find_element_by_xpath('//*[@id="funtype_click_center_right_list_category_0100_0100"]').click()

driver.find_element_by_xpath('//*[@id="funtype_click_center_right_list_sub_category_each_0100_0106"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="funtype_click_bottom_save"]').click()

driver.find_element_by_xpath('//*[@id="cottype_list"]').click()
driver.find_element_by_xpath('//*[@title="外资（欧美）"]').click()

driver.find_element_by_xpath('//*[@id="workyear_list"]').click()
driver.find_element_by_xpath('//*[@title="1-3年"]').click()

time.sleep(1)
driver.find_element_by_xpath('//*[@class="btnbox p_sou"]/span').click()

driver.implicitly_wait(10)
time.sleep(1)

jobs = driver.find_elements_by_xpath('//*[@id="resultList"]/div[@class="el"]')
for job in  jobs:
    print(job.text.replace('\n', '|'))


driver.quit()