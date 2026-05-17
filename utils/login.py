from selenium.webdriver.common.by import By

def login(driver):

    driver.get("https://saucedemo.com")
    
    driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]' ).click()