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

def test_regis(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@href='/account/register']").click()
    time.sleep(2)
    driver.find_element(By.ID,"last_name").send_keys("Lê")
    time.sleep(1)
    driver.find_element(By.ID,"first_name").send_keys("Trọng Luân")
    time.sleep(1)
    driver.find_element(By.ID,"birthday").send_keys("10/23/2003")
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("letrongluan222@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("23102003Luan")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(5)
    assert "https://baycollection.vn/account" in driver.current_url
    
def test_regis_valid_email(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.XPATH, "//a[@href='/account/register']").click()
    time.sleep(2)
    driver.find_element(By.ID,"last_name").send_keys("Lê")
    time.sleep(1)
    driver.find_element(By.ID,"first_name").send_keys("Trọng Luân")
    time.sleep(1)
    driver.find_element(By.ID,"birthday").send_keys("10/23/2003")
    time.sleep(1)
    driver.find_element(By.ID,"email").send_keys("letrongluan2@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID,"password").send_keys("23102003Luan")
    time.sleep(1)
    driver.find_element(By.XPATH,"//input[@type='submit']").click()
    time.sleep(5)
    error_message = driver.find_element(By.CLASS_NAME, "errors").text
    assert "Email đã tồn tại" in error_message
