import time
import datetime
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

option = ChromeOptions()
# option.add_argument('--headless')
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
driver.maximize_window()

driver.get('https://yes.vanderbilt.edu')
driver.implicitly_wait(5)
driver.find_element_by_id('username').send_keys('USERNAME')
driver.find_element_by_id('password').send_keys('PASSWORD')
driver.find_element_by_xpath('/html/body/div/div[2]/div/form/div[6]/a').click()
driver.implicitly_wait(5)
driver.get('COURSE SEARCH LINK')
driver.implicitly_wait(5)
driver.find_element_by_id('savedHours').click()


def select_course():
    time.sleep(0.5)
    driver.find_element_by_id('COURSE BUTTONS').click()
    driver.find_element_by_xpath('E or W').click()


select_course()

while driver.find_element_by_id('enrollmentButtons').text == '':
    time_stamp = datetime.datetime.now()
    print(time_stamp.strftime('%Y-%m-%d %H:%M:%S')+' You Do Not Have Enough Permission to Enroll At This Time.')
    try:
        driver.refresh()
        driver.implicitly_wait(5)
        driver.find_element_by_id('savedHours').click()
        select_course()
    except:
        driver.refresh()
        driver.implicitly_wait(5)
        driver.find_element_by_id('savedHours').click()

time_stamp = datetime.datetime.now()
print(time_stamp.strftime('%Y-%m-%d %H:%M:%S')+' You Can Begin Your Enrollment Now!')
