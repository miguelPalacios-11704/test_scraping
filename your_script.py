from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Configura las opciones de Chrome
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Conéctate al servidor remoto Selenium Grid
driver = webdriver.Remote(
    command_executor="http://selenium-server:4444/wd/hub",
    options=chrome_options
)

# Prueba: Abre una página y realiza acciones
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Llena un formulario de ejemplo
driver.find_element(By.NAME, "my-text").send_keys("John Doe")
driver.find_element(By.NAME, "my-password").send_keys("1234")
driver.find_element(By.NAME, "my-textarea").send_keys("hola a la clase de fuentes de datos")
driver.find_element(By.NAME, "my-checkbox").click()
driver.find_element(By.NAME, "my-select").find_element(By.XPATH, "//option[@value='2']").click()
driver.find_element(By.ID, "my-radio-2").click()
driver.find_element(By.CSS_SELECTOR, "button").click()

print("Form submitted successfully!")
driver.quit()

