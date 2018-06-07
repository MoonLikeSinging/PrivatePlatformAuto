from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"D:\Android\ChromeDriver\chromedriver.exe")
driver.implicitly_wait(3)
driver.get("https://private.kiwisec.com")
driver.maximize_window()
email = driver.find_element_by_id('email')
pwd = driver.find_element_by_id('password')
email.send_keys('luyue@kiwisec.com')
pwd.send_keys('kiwi888zx')
time.sleep(2)

signinbutton = driver.find_element_by_class_name('btn-primary')
signinbutton.click()
time.sleep(10)
menu_detection_report = driver.find_element_by_id('menu-detection-report')


menu_detection_report.click()
time.sleep(3)
add_android_app = driver.find_element_by_class_name("btn-fileupload")
print(add_android_app.text)
add_android_app.click()
