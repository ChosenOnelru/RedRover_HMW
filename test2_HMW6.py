from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# 6.2

def open_page():
    browser.get('http://suninjuly.github.io/cats.html')

# XPATH селекторы

    view_p = browser.find_element(By.XPATH, "/ html / body / main / div / div / div / div[5] / div / div / p") # ищем элемент
    print(view_p) # печатаем полученный список элементов
    print(view_p.text) # печатаем текст элемента
    assert view_p.text == 'Fully charged cat'

    view_p1 = browser.find_element(By.XPATH, "//div[5] / div / div / p") # ищем элемент
    print(view_p1) # печатаем полученный список элементов
    print(view_p1.text) # печатаем текст элемента
    assert view_p1.text == 'Fully charged cat'

    view_p2 = browser.find_element(By.XPATH, "//*[contains(text(), 'Fully charged cat')]")  # ищем элемент
    print(view_p2)  # печатаем полученный список элементов
    print(view_p2.text)  # печатаем текст элемента
    assert view_p2.text == 'Fully charged cat'

    view_p3 = browser.find_element(By.XPATH, "//div[5]/div/div/*[@class='card-text']")  # ищем элемент
    print(view_p3)  # печатаем полученный список элементов
    print(view_p3.text)  # печатаем текст элемента
    assert view_p3.text == 'Fully charged cat'

    view_p4 = browser.find_element(By.XPATH, "//p[text()='Fully charged cat']")  # ищем элемент
    print(view_p4)  # печатаем полученный список элементов
    print(view_p4.text)  # печатаем текст элемента
    assert view_p4.text == 'Fully charged cat'

    view_button5 = browser.find_element(By.XPATH, "//*[@class='card-text'][contains(text(), 'Fully')]")  # ищем элемент
    print(view_button5)  # печатаем полученный список элементов
    print(view_button5.text)  # печатаем текст элемента
    assert view_button5.text == 'Fully charged cat'

# CSS селекторы

    view_p_css = browser.find_element(By.CSS_SELECTOR, "div:nth-child(5) > div > div > p")  # ищем элемент
    print(view_p_css)  # печатаем полученный список элементов
    print(view_p_css.text)  # печатаем текст элемента
    assert view_p_css.text == 'Fully charged cat'

    view_p_css1 = browser.find_element(By.CSS_SELECTOR, "div:nth-child(5) > div > div > .card-text")  # ищем элемент
    print(view_p_css1)  # печатаем полученный список элементов
    print(view_p_css1.text)  # печатаем текст элемента
    assert view_p_css1.text == 'Fully charged cat'

    view_p_css2 = browser.find_element(By.CSS_SELECTOR, "body > main > div > div > div > div:nth-child(5) > div > div > p")  # ищем элемент
    print(view_p_css2)  # печатаем полученный список элементов
    print(view_p_css2.text)  # печатаем текст элемента
    assert view_p_css2.text == 'Fully charged cat'

def test_open_page():
    open_page()


# DOM
# <div class="album py-5 bg-light">
# 	        <div class="container">
#
# 	          <div class="row">
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img id="bullet" name="bullet-cat" data-type="animal" class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/bullet_cat.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p class="card-text">Bullet cat</p>
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/serious_cat.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p class="card-text second">Serious cat</p>
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/lenin_cat.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p id="politic" class="card-text lenin-cat" name="Vova" data-name="Vladimir">Lenin cat</p>
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
#
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/cougar-cat-memes.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p class="card-text">Cougar cat</p>
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/fully-charged-cat.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p class="card-text">Fully charged cat</p>                                                            # найти этот элемент
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
# 	            <div class="col-sm-4">
# 	              <div class="card mb-4 box-shadow">
# 	                <img class="card-img-top" data-src="holder.js/100px225?theme=thumb&amp;bg=55595c&amp;fg=eceeef&amp;text=Thumbnail" alt="Thumbnail [100%x225]" src="images/i-love-you-so-much-cat-memes.jpg" data-holder-rendered="true">
# 	                <div class="card-body">
# 	                  <p class="card-text">I love you so much</p>
# 	                  <div class="d-flex justify-content-between align-items-center">
# 	                    <div class="btn-group">
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
# 	                      <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
# 	                    </div>
# 	                    <small class="text-muted">9 mins</small>
# 	                  </div>
# 	                </div>
# 	              </div>
# 	            </div>
# 	          </div>
# 	        </div>
#       	</div>