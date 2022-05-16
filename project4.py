from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys  # 键盘
from selenium.webdriver.common.action_chains import  ActionChains  #鼠标

driver = webdriver.Chrome(executable_path='D:\ProgramData\Miniconda3\chromedriver.exe')

#打开百度
driver.get("https://www.baidu.com/")

driver.maximize_window() #最大化窗口
driver.implicitly_wait(5) #等待五秒

driver.find_element_by_xpath("//*[@id='kw']").send_keys("baidu")           # 利用元素属性（id）定位
sleep(2)
driver.find_element_by_id("kw").clear()
sleep(2)
driver.find_element_by_xpath("//*[@name='wd']").send_keys("python")      # 利用元素属性（name）定位

sleep(2)
driver.find_element_by_xpath("//*[@class='s_ipt']") .send_keys("selenium")    # 利用元素属性（class）定位

sleep(2)
driver.find_element_by_xpath("//*[@autocomplete='off']").send_keys("selenium")
sleep(2)
driver.find_element_by_name("wd").send_keys(Keys.CONTROL,'A')
sleep(2)
driver.find_element_by_name("wd").send_keys(Keys.CONTROL,'X')
sleep(2)
driver.find_element_by_name("wd").send_keys(Keys.CONTROL,'V')
sleep(2)
driver.find_element_by_name("wd").send_keys(Keys.CONTROL,'V')
element=driver.find_element_by_xpath("//*[@id='su']")
ActionChains(driver).click(element).perform()
sleep(2)
driver.find_element_by_xpath("//*[@value='百度一下']").click()