from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


serv_obj = Service("C:\WebDrivers\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=serv_obj)
driver.get("https://www.amazon.com.tr/")
driver.maximize_window()
driver.implicitly_wait(5)
action = ActionChains(driver)

# Accept Cookies
driver.find_element(By.XPATH, "//input[@data-cel-widget='sp-cc-accept']").click()
action.move_to_element(driver.find_element(By.XPATH, "//span[contains(normalize-space(),'Hesap ve Listeler')]"))
action.perform()
driver.find_element(By.XPATH, "//div[@id='nav-flyout-ya-newCust']//a[@class='nav-a'][normalize-space()='Üye olun.']").click()
driver.find_element(By.XPATH, "//input[@id='ap_customer_name']").send_keys("Miray Sav")
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("miraytest123@gmail.com")
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Test123.")
driver.find_element(By.XPATH, "//input[@id='ap_password_check']").send_keys("")
driver.find_element(By.XPATH, "//input[@name='legalMarketingCheckBox']").click()
driver.find_element(By.XPATH, "//input[@aria-labelledby='auth-continue-announce']").click()
#Şifre tekrarı çalışıyor