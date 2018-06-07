import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import os
import random
app_download = []
current_path = os.path.abspath('.')
driver = webdriver.Chrome(current_path + '\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(3)

base_link = ' '


def save_app_download_info():
    bs = BeautifulSoup(driver.page_source, 'html.parser')
    download_links_info = bs.find_all('a', attrs={'class':re.compile('dbtn \S+')})

    for link in download_links_info:
        download_link = (re.search(r'url=http://\S+.apk', str(link)).group())[4:]
        app_download.append(download_link)


def random_download_one_app():
    count = len(app_download)
    num = random.randint(0, count)
    link = app_download[num]
    file = urllib.request.urlopen(link)
    data = file.read()
    with open(current_path + r'\test.apk', 'wb') as code:
        code.write(data)


if __name__ == '__main__':
    for i in range(5):
        driver.get(base_link + str(i+1))
        time.sleep(3)
        save_app_download_info()
    random_download_one_app()
    driver.quit()




