from selenium.webdriver.common.by import By

def test_page_contains_add_to_basket_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # time.sleep(30)
    add_to_cart_button = browser.find_elements(By.XPATH, "//button[contains(@class, 'btn-add-to-basket')]")
    assert len(add_to_cart_button) > 0
