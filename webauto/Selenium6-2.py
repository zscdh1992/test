from selenium import  webdriver
import win32com.client
import win32api
import win32con
import  time



driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.maximize_window()
driver.get('https://tinypng.com/')
driver.implicitly_wait(10)

driver.find_element_by_xpath('//*[@class="target"]').click()
time.sleep(1)

shell = win32com.client.Dispatch("WScript.shell")
shell.SendKeys(r"D:\preview.jpg"+"\n")
win32api.keybd_event(13,0,0,0)
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)




driver.quit()