from selenium import  webdriver
from time import  sleep
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

webdriver = webdriver.Chrome(r'D:\ProgramData\Miniconda3chromedriver.exe')
webdriver.get('http://192.168.64.8/bsams/front/login.do')
webdriver.implicitly_wait(30)
webdriver.maximize_window()
webdriver.find_element_by_id('taskId').send_keys('802')
sleep(2)
webdriver.find_element_by_css_selector('#loginName').send_keys('student')
webdriver.find_element_by_xpath('//*[@id="password"]').send_keys('student')
webdriver.find_elements_by_class_name('validcode')[0].send_keys('shtd')
ActionChains(webdriver).send_keys(Keys.ENTER).perform()