import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_auth_page(driver):
    driver.find_element(By.CSS_SELECTOR,'html > body > main > section > h1 > a').click()
    time.sleep(7)

    enter_email = driver.find_element(By.XPATH,
                                      '//*[@id="id_login"]')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(4)

    enter_password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    enter_password.send_keys('1880zOk?')
    time.sleep(6)

    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/form[1]/button[1]').click()

    assert driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/h1[1]')


def test_auth_page_forgotten_password(driver):
    driver.find_element(By.CSS_SELECTOR, 'html > body > main > section > h1 > a').click()
    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/div[1]/a[1]').click()
    time.sleep(3)


    enter_email = driver.find_element(By.XPATH, '//*[@id="id_email"]')
    enter_email.send_keys('asya_yepifanova@mail.ru')
    time.sleep(7)

    auth = driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/form[1]/button[1]')
    auth.click()
    time.sleep(3)

    assert driver.find_element(By.CSS_SELECTOR, 'html > body > p')


def test_auth_page_yandex(driver):
    driver.find_element(By.CSS_SELECTOR, 'html > body > main > section > h1 > a').click()
    time.sleep(4)


    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/div[2]/a[1]')
    time.sleep(3)

    assert driver.find_element(By.CSS_SELECTOR, 'html > body')



def test_auth_page_github(driver):
    driver.find_element(By.CSS_SELECTOR, 'html > body > main > section > h1 > a').click()
    time.sleep(4)


    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/div[2]/a[2]')
    time.sleep(3)

    assert driver.find_element(By.CSS_SELECTOR, 'html > body')



