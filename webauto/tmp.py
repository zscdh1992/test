from selenium import webdriver

driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

weather = driver.find_element_by_class_name('forecastBox')
weather1 =''
count =-1
citys = weather.find_elements_by_tag_name('a')
for city in citys:
count += 1
if count%4 ==0:
weather1= weather1+'|'+city.text
else:
weather1 = weather1+'-'+city.text


lowweather =10000
city_weather = weather1.split('|')
city_list =[]

for city in city_weather:
if city !='':
print(city)
city_name = city.split('--')[0]
cityweather = int(city.split('--')[1].split('-')[0].split('℃')[0])
if cityweather < lowweather:
lowweather = cityweather
if city_list==[]:
city_list.append(city_name)
else:
city_list = []
city_list.append(city_name)
elif cityweather == lowweather:
city_list.append(city_name)
else:
city_list = city_list

print('温度最低为%s℃, 城市有%s' % (lowweather, ' '.join(city_list)))

driver.quit()