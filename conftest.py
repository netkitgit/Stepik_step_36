# Для корректной работы требуется установка:
# pip install pytest
# pip install -U selenium
# pip install webdriver_manager

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    print("\nStart CHROME browser for test...")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield browser
    print("\nQuite browser...")
    browser.quit()
