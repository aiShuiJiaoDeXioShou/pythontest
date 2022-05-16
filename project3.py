# -*- coding: UTF-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

wd = webdriver.Chrome(r'D:\ProgramData\Miniconda3\chromedriver.exe')
wd.get('http://192.168.64.8/bsams/front/login.do')
wd.implicitly_wait(30)
wd.maximize_window()
wd.find_element_by_id('taskId').send_keys('810')
wd.find_element_by_css_selector('#loginName').send_keys('student')
wd.find_element_by_xpath('//*[@id="password"]').send_keys('student')
wd.find_element_by_class_name('validcode').send_keys('shtd')
ActionChains(wd).send_keys(Keys.ENTER).perform()
sleep(2)
wd.find_element_by_id('leftmenu_asset_user').click()
wd.find_element_by_class_name('nickname').clear()
wd.find_element_by_class_name('nickname').send_keys('12345678911')
wd.find_element_by_class_name('button_fujian').click()
sleep(2)
alert = wd.switch_to_alert()
alert.accept()
ActionChains(wd).click(wd.find_elements_by_class_name('right')[0]).perform()
