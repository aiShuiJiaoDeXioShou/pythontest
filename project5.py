from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys  # 键盘
from selenium.webdriver.common.action_chains import  ActionChains  #鼠标

wb = webdriver.Chrome()
wb.get("https://www.baidu.com")
wb.maximize_window()
sleep(5)
input_wb = wb.find_element_by_id("kw")
wb.find_element_by_id("kw").send_keys("python")
input_wb.send_keys(Keys.CONTROL,'A')
sleep(2)
input_wb.send_keys(Keys.CONTROL,'C')
sleep(2)
input_wb.send_keys(Keys.CONTROL,'V')
sleep(2)
input_wb.send_keys(Keys.CONTROL,'V')
sleep(2)
input_wb.click()
sleep(1)
ok_but = wb.find_element_by_id("su")
sleep(1)

#这个是使用xpath，寻找输入框
wb.find_element_by_xpath("//*[@id='kw']").send_keys("python")
wb.find_element_by_css_selector("#kw").send_keys("pyhon")

#控制事件
ok_but.click() #单击
# ActionChains(wb).double_click(ok_but).perform() #双击
sleep(4)
ActionChains(wb).context_click(wb.find_element_by_css_selector(".content-right_8Zs40")).perform()#右击



