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

def test_valid_login(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.ID, "login-customer[email]").send_keys("letrongluan2@gmail.com")
    driver.find_element(By.ID, "login-customer[password]").send_keys("Luan23102003#")
    driver.find_element(By.ID, "form_submit-login").click()
    time.sleep(2)
    assert "https://baycollection.vn/account" in driver.current_url
    
def test_invalid_login(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.ID, "login-customer[email]").send_keys("invalid_user")
    driver.find_element(By.ID, "login-customer[password]").send_keys("wrong_password")
    driver.find_element(By.ID, "form_submit-login").click()
    time.sleep(5)
def test_emty_username(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.ID, "login-customer[email]").send_keys("")
    driver.find_element(By.ID, "login-customer[password]").send_keys("Luan23102003#")
    driver.find_element(By.ID, "form_submit-login").click()
    time.sleep(2)
    
def test_emty_password(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.ID, "login-customer[email]").send_keys("letrongluan2@gmail.com")
    driver.find_element(By.ID, "login-customer[password]").send_keys("")
    driver.find_element(By.ID, "form_submit-login").click()
    time.sleep(2)
    
def test_logout(driver):
    driver.get("https://baycollection.vn/")
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.ID, "login-customer[email]").send_keys("letrongluan2@gmail.com")
    driver.find_element(By.ID, "login-customer[password]").send_keys("Luan23102003#")
    driver.find_element(By.ID, "form_submit-login").click()
    time.sleep(2)
    driver.find_element(By.ID,"site-account-handle").click()
    time.sleep(5)
    driver.find_element(By.XPATH,"//a[@href='/account/logout']").click()
    time.sleep(5)
    assert "https://baycollection.vn/" in driver.current_url


