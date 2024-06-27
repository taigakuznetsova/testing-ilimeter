import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as WDW
from selenium.webdriver.support import expected_conditions as EC


def test_auth_page_wrong_password(driver):
    driver.find_element(By.CSS_SELECTOR,'html > body > main > section > h1 > a').click()

    enter_email = driver.find_element(By.XPATH,
                                      '//*[@id="id_login"]')
    enter_email.send_keys('taiga.taiga@mail.com')

    enter_password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    enter_password.send_keys('0438513FzZsWM')

    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/form[1]/button[1]').click()

    assert driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/h1[1]')



def test_auth_page_wrong_email(driver):
    driver.find_element(By.CSS_SELECTOR,'html > body > main > section > h1 > a').click()

    enter_email = driver.find_element(By.XPATH,
                                      '//*[@id="id_login"]')
    enter_email.send_keys('asya_sosnova@mail.ru')

    enter_password = driver.find_element(By.XPATH, '//*[@id="id_password"]')
    enter_password.send_keys(' 1880zOk?')

    driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/div[1]/div[1]/form[1]/button[1]').click()

    assert driver.find_element(By.XPATH, '//*[@id="main-content"]/main[1]/h1[1]')
