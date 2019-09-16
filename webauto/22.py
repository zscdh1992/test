from selenium import  webdriver
import  time
import datetime


def doSth():
    # 把程序放在这个类里
    print('开始签到')
    driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
    driver.maximize_window()
    driver.get('http://10.0.20.74:8010/eoffice10/client/app/web/login.html')
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('//*[@name="user-account"]').clear()
    driver.find_element_by_xpath('//*[@name="user-account"]').send_keys(account)
    time.sleep(1)
    driver.find_element_by_xpath('//*[@type="submit"]').click()
    driver.implicitly_wait(10)
    time.sleep(10)
    driver.find_element_by_xpath('//*[@id="content-wrapper"]/ui-view/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/button/span').click()


# 一般网站都是1:00点更新数据，所以每天启动
def main(h,m):
    while True:
        now = datetime.datetime.now()
        # print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
            doSth()
        # 每隔60秒检测一次
        time.sleep(60)


account = input('请输入帐号：')
h= int(input('h：'))
m= int(input('m：'))
main(h,m)


