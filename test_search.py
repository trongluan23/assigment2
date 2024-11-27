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
def test_search(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-search-handle").click()
    time.sleep(2)
    driver.find_element(By.ID,"inputSearchAuto").send_keys("áo")
    driver.find_element(By.ID,"search-header-btn").click()
    time.sleep(5)
def test_search_special(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-search-handle").click()
    time.sleep(2)
    driver.find_element(By.ID,"inputSearchAuto").send_keys("wasedrftgyhujikolp;ơedrfgtyhujikolp;ỡdcfvgbhnjmk")
    driver.find_element(By.ID,"search-header-btn").click()
    time.sleep(5)
    