from tkinter import *
from selenium import  webdriver
import  time
import datetime
import threading
import tkinter.messagebox

def thread_it(func, *args):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func, args=args)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！


def callback():
    tkinter.messagebox.showinfo("提示", "启动成功！")


def login():
    print('11')
    account = text1.get()
    h = int(text2.get())
    m = int(text3.get())
    print(account,h,m)
    while True:
        now = datetime.datetime.now()
        print(now.hour, now.minute)
        if now.hour == h and now.minute == m:
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
            driver.find_element_by_xpath(
                '//*[@id="content-wrapper"]/ui-view/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/button/span').click()

        # 每隔60秒检测一次
        time.sleep(60)



top=tkinter.Tk(className='自动登录')
#定义窗体的大小，是400X200像素
top.geometry('400x200')


label_user = Label(text='请输入帐号：',bg='green')
label_user.grid(row=0,column=0,sticky=W)
label_user.pack()
#输入框1
text1 = tkinter.StringVar()
text1.set('')
entry = tkinter.Entry(top)
entry['textvariable'] = text1
entry.pack()

user=Entry()
user.grid(row=0,column=1)
label_h = tkinter.Label(top)
label_h['text'] = '请输入几点启动：'
label_h.pack()
#输入框2
text2 = tkinter.StringVar()
text2.set('')
entry = tkinter.Entry(top)
entry['textvariable'] = text2
entry.pack()

label_m = tkinter.Label(top)
label_m['text'] = '请输入几分启动：'
label_m.pack()
#输入框3
text3 = tkinter.StringVar()
text3.set('')
entry = tkinter.Entry(top)
entry['textvariable'] = text3
entry.pack()
#
# btn = tkinter.Button(top,text='确定',command=lambda :thread_it(callback)).pack()
btn = tkinter.Button(top,text='确定',command=lambda :thread_it(login)).pack()

#进入消息循环体
top.mainloop()