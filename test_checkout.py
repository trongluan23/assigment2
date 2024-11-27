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

def test_checkout_no_product(driver):
    driver.get("https://baycollection.vn/")
    time.sleep(2)
    driver.find_element(By.ID,"site-cart-handle").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[@href='/checkout']").click()
    time.sleep(2)
    driver.find_element(By.CLASS_NAME,"btncart-checkout").click()
    time.sleep(5)
    assert "https://baycollection.vn/cart" in driver.current_url
    
def test_checkout(driver):
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
    driver.find_element(By.XPATH,"//a[@href='/checkout']").click()
    time.sleep(5)
    driver.find_element(By.ID,"billing_address_full_name").send_keys("Lê Trọng Luân")
    driver.find_element(By.ID,"checkout_user_email").send_keys("letrongluan2@gmail.com")
    driver.find_element(By.ID,"billing_address_phone").send_keys("0374370617")
    driver.find_element(By.ID,"billing_address_address1").send_keys("Hồ Chí Minh")
    driver.find_element(By.ID,"customer_shipping_province").click()

    
    
