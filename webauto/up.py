from selenium import webdriver

driver = webdriver.Chrome(r"E:\webdriver\chromedriver.exe")
driver.get('http://music.taihe.com/top/new')

TopNew = driver.find_element_by_id("songListWrapper").find_element_by_tag_name("ul").find_elements_by_tag_name('li')

for up in TopNew:
    if up.find_elements_by_class_name("up")!= []:
        song = up.find_element_by_class_name("song-title").find_element_by_tag_name("a").text
        author = up.find_element_by_class_name("author_list").text
        print('{:10s}:{}'.format(song, author))

driver.quit()