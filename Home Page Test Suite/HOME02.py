from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import switch_to
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
driver.find_element(By.XPATH, "//span[.='Giriş yap']").click()
driver.find_element(By.XPATH, "//input[@id='ap_email']").send_keys("miraytest123@gmail.com")
driver.find_element(By.XPATH, "//input[@id='continue']").click()
driver.find_element(By.XPATH, "//input[@id='ap_password']").send_keys("Test123.")
driver.find_element(By.XPATH, "//input[@name='rememberMe']").click()
driver.find_element(By.XPATH, "//input[@id='signInSubmit']").click()
#Side menu check
driver.find_element(By.XPATH, "//i[@class='hm-icon nav-sprite']").click()
driver.find_element(By.XPATH, "//div[.='tümünü görüntüle']").click()
driver.find_element(By.XPATH, "//a[@data-menu-id='10']").click()
driver.find_element(By.XPATH, "//a[.='Cilt Bakımı']").click()

# Side menu is working