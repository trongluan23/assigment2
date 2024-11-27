import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
def test_navigation(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@href='/collections/all']").click()
    time.sleep(5)
