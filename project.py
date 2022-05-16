from selenium import webdriver

dirver = webdriver.Chrome("D:\ProgramData\Miniconda3\chromedriver.exe")
dirver.get("https://www.baidu.com/")
dirver.maximize_window()
dirver.find_element_by_xpath('//*[@id="kw"]').send_keys("bilibili")
dirver.find_element_by_xpath('//*[@id="su"]').click()
