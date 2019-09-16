from tkinter import *
from selenium import  webdriver
import  time
import datetime
import threading
import tkinter.messagebox
import random


option = webdriver.ChromeOptions()
option.add_argument("disable-infobars")

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！


def get_week_day(date):
  week_day_dict = {
    0 : '星期一',
    1 : '星期二',
    2 : '星期三',
    3 : '星期四',
    4 : '星期五',
    5 : '星期六',
    6 : '星期天',
  }
  day = date.weekday()
  return week_day_dict[day]

def callback():
    tkinter.messagebox.showinfo("提示", "启动成功！")


def login():
    account = user.get()
    h = i_h.get()
    m = i_m.get()
    get_week_day(datetime.datetime.now())
    # h1 = i_h1.get()
    # m1 = i_m1.get()
    if account == '':
        tkinter.messagebox.showinfo("提示", "未输入帐号！")
    elif h == '' or m == '':
        tkinter.messagebox.showinfo("提示", "未设置时间！")
    elif h.isdigit() == False or m.isdigit() == False :
        tkinter.messagebox.showinfo("提示", "请输入数字！")
    else:

        label.config(text="已启动")
        while True:
            now = datetime.datetime.now()
            account = user.get()
            h = i_h.get()
            m = i_m.get()
            week_day = get_week_day(datetime.datetime.now())
            if week_day =='星期一'or week_day =='星期二' or week_day =='星期三' or week_day =='星期四' or week_day =='星期五':
                if (now.hour == int(h) and now.minute == int(m) ):
                    driver = webdriver.Chrome(executable_path=r"E:\webdriver\chromedriver.exe",chrome_options=option)
                    driver.maximize_window()
                    driver.get('http://10.0.20.74:8010/eoffice10/client/app/web/login.html')
                    driver.implicitly_wait(20)
                    driver.find_element_by_xpath('//*[@name="user-account"]').clear()
                    driver.find_element_by_xpath('//*[@name="user-account"]').send_keys(account)
                    time.sleep(2)
                    driver.find_element_by_xpath('//*[@type="submit"]').click()
                    driver.implicitly_wait(10)
                    time.sleep(10)
                    driver.find_element_by_xpath('//*[@id="content-wrapper"]/ui-view/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/button/span').click()
                    time.sleep(5)
                    signintime=driver.find_element_by_xpath('//*[@ng-if="directiveConfig.signInTime"]').text
                    signouttime=driver.find_element_by_xpath('//*[@ng-if="directiveConfig.signOutTime"]').text
                    time.sleep(5)
                    with open('./log.txt','a') as f:
                        f.write('\n上班：{}下班：{}'.format(signintime,signouttime))
                    driver.quit()

            # 每隔60秒检测一次
            time.sleep(60)



root=Tk()
root.geometry('300x200')
root.title("登录")
label_user=Label(text='用户名:')
label_h=Label(text='启用时:')
label_m=Label(text='启用分:')
# label_h1=Label(text='下班启用时:')
# label_m1=Label(text='下班启用分:')
user=Entry()
i_h=Entry()
i_m=Entry()
# i_h1=Entry()
# i_m1=Entry()
# row,column,sticky
label_user.grid(row=0,column=0,sticky=W) #一个有sticky,一个没有sticky，以作区分
label_h.grid(row=1,column=0,sticky=W)
label_m.grid(row=2,column=0,sticky=W)
# label_h1.grid(row=1,column=2,sticky=W)
# label_m1.grid(row=2,column=2,sticky=W)
label=Label(text="未启动！",bg='blue')
label.grid(row=4,column=2,sticky=W)
# rowspan,columnspan
user.grid(row=0,column=1)
i_h.grid(row=1,column=1)
i_m.grid(row=2,column=1)
# i_h1.grid(row=1,column=3)
# i_m1.grid(row=2,column=3)

# 下面主要是将第一列拉大来显示上面sticky的效果


btn = tkinter.Button(root,text='确定',command=lambda :thread_it(login))
btn.grid(row=3,column=0,rowspan=2,columnspan=2,padx=5, pady=5)



root.mainloop()