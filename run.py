from time import time

import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

opts = Options()
opts.headless = True
assert opts.headless

driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver",
                          options=opts)
driver.get("https://healthscreening.schools.nyc/?type=G")

try:
    guest_radio = driver.find_element_by_xpath(
        '//input[@id="guest_isStudent" and @class="custom-control-input"]')
    driver.execute_script("arguments[0].click();", guest_radio)

    driver.find_element_by_id("guest_first_name").send_keys("Jan")
    driver.find_element_by_id("guest_last_name").send_keys("Gonzalvo")
    driver.find_element_by_id("guest_email").send_keys(
        "xavigonzalvo@gmail.com")

    button = driver.find_element_by_xpath(
        '//*[@id="guest_identity_form"]/div[2]/div[13]/span/span/span[2]/span')
    button.click()
    school_input = driver.find_element_by_xpath(
        '//*[@id="Location-list"]/span/input')
    time.sleep(1)
    school_input.send_keys("adolph s")
    time.sleep(1)
    school_input.send_keys(Keys.ENTER)

    driver.find_element_by_id("guest_location_floor").send_keys(
        "0")

    driver.find_element_by_xpath(
        '//*[@id="btnDailyScreeningSubmit"]/button').click()

    time.sleep(2)

    element = driver.find_element_by_xpath('//*[@id="spyes"]')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)

    element = driver.find_element_by_xpath('//*[@id="pq1no"]')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)

    element = driver.find_element_by_xpath('//*[@id="pq2no"]')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)

    element = driver.find_element_by_xpath('//*[@id="pq3no"]')
    driver.execute_script("arguments[0].click();", element)

    time.sleep(1)

    driver.find_element_by_xpath(
        '//*[@id="questions_layout"]/div[6]/div[1]/button').click()

except Exception as e:
    print("Error", e)
finally:
    user_choice = input('Please click ENTER button to close application')
    if not user_choice:
        print("ABORTED")
        driver.close()
