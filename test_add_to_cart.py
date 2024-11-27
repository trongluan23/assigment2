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
    
def test_add_to_cart(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-search-handle").click()
    time.sleep(2)
    driver.find_element(By.ID,"inputSearchAuto").send_keys("áo")
    driver.find_element(By.ID,"search-header-btn").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/products/ao-thun-nam-ta02-kem']").click()
    time.sleep(2)
    driver.find_element(By.ID,"add-to-cart").click()
    time.sleep(5)
     
def test_view_cart(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-search-handle").click()
    time.sleep(2)
    driver.find_element(By.ID,"inputSearchAuto").send_keys("áo")
    driver.find_element(By.ID,"search-header-btn").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/products/ao-thun-nam-ta02-kem']").click()
    time.sleep(2)
    driver.find_element(By.ID,"add-to-cart").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/cart']").click()
    time.sleep(5)
    assert "https://baycollection.vn/cart" in driver.current_url

def test_remove(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-search-handle").click()
    time.sleep(2)
    driver.find_element(By.ID,"inputSearchAuto").send_keys("áo")
    driver.find_element(By.ID,"search-header-btn").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/products/ao-thun-nam-ta02-kem']").click()
    time.sleep(2)
    driver.find_element(By.ID,"add-to-cart").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/cart']").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/cart/change?line=1&quantity=0']").click()
    time.sleep(5)
    assert "https://baycollection.vn/cart" in driver.current_url