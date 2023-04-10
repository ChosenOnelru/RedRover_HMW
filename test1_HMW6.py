from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 6.1

def open_page():
    browser.get('http://suninjuly.github.io/xpath_examples')

# XPATH селекторы

    view_button = browser.find_element(By.XPATH, "/html/body/div[2]/button[3]") # ищем элемент
    print(view_button) # печатаем полученный список элементов
    print(view_button.text) # печатаем текст элемента
    assert view_button.text == 'Gold'

    view_button0 = browser.find_element(By.XPATH, "//div[2]/button[3]") # ищем элемент
    print(view_button0) # печатаем полученный список элементов
    print(view_button0.text) # печатаем текст элемента
    assert view_button0.text == 'Gold'

    view_button1 = browser.find_element(By.XPATH, "//*[contains(text(), 'Gold')]") # ищем элемент
    print(view_button1) # печатаем полученный список элементов
    print(view_button1.text) # печатаем текст элемента
    assert view_button1.text == 'Gold'

    view_button2 = browser.find_element(By.XPATH, "//div[2]/*[@class='btn'][3]")  # ищем элемент
    print(view_button2)  # печатаем полученный список элементов
    print(view_button2.text)  # печатаем текст элемента
    assert view_button2.text == 'Gold'

    view_button3 = browser.find_element(By.XPATH, "//button[text()='Gold']")  # ищем элемент
    print(view_button3)  # печатаем полученный список элементов
    print(view_button3.text)  # печатаем текст элемента
    assert view_button3.text == 'Gold'

    view_button4 = browser.find_element(By.XPATH, "//*[@class='btn'][contains(text(), 'Go')]")  # ищем элемент
    print(view_button4)  # печатаем полученный список элементов
    print(view_button4.text)  # печатаем текст элемента
    assert view_button4.text == 'Gold'

# CSS селекторы

    view_button_css = browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > button:nth-of-type(3)")  # ищем элемент
    print(view_button_css)  # печатаем полученный список элементов
    print(view_button_css.text)  # печатаем текст элемента
    assert view_button_css.text == 'Gold'

    view_button_css1 = browser.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .btn:nth-of-type(3)")  # ищем элемент
    print(view_button_css1)  # печатаем полученный список элементов
    print(view_button_css1.text)  # печатаем текст элемента
    assert view_button_css1.text == 'Gold'

def test_open_page():
    open_page()

# DOM
# <html><head>
#     <script src="jquery_min.js"></script>
#     <title>Welcome!</title>
#     <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
# <script src="chrome-extension://mooikfkahbdckldjjndioackbalphokd/assets/prompt.js"></script></head>
#
# <body class="bg-light" cz-shortcut-listen="true">
# <div style="padding-top: 90px;">
#
#
# <button class="btn">Submit</button>
# <button class="btn">Submit</button>
# <button class="btn">Submit</button>
# <button class="btn">Submit</button>
# </div>
# <div style="padding-top: 90px;">
# <button class="btn">Submit</button>
# <button class="btn">Submit</button>
# <button class="btn">Gold</button> # найти этот элемент
# <button class="btn">Submit</button>
# </div>
#
#
# </body></html>