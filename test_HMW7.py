import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import my_email, my_password

def test_open_page(browser):
    browser.get('https://openweathermap.org/') # открыть url
    assert 'openweathermap' in browser.current_url # проверка наличия строки в url

def test_sing_in_empty_fields(browser):
    time.sleep(5)
    browser.find_element(By.XPATH, '//a[contains(@href, "sign_in")]').click()
    browser.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    alert1 = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]')
    assert alert1.text == 'Invalid Email or password.'

def test_sing_in_positive(browser):
    email_form = browser.find_element(By.XPATH, '//*[@id = "user_email"]')
    email_form.click()
    email_form.send_keys(my_email)
    password_form = browser.find_element(By.XPATH, '//*[@id = "user_password"]')
    password_form.click()
    password_form.send_keys(my_password)
    remember_checkbox = browser.find_element(By.XPATH, '//*[@id = "user_remember_me"]')
    assert remember_checkbox.is_selected() == False
    browser.find_element(By.XPATH, '//*[@id="new_user"]/input[3]').click()
    browser.implicitly_wait(15)
    assert 'home.openweathermap' in browser.current_url
    alert = browser.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div/div/div[2]')
    assert alert.text == 'Signed in successfully.'
