# coding=utf-8
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import logging

logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.debug('Starting script...')


# Todo esto evita errores al correr el chromedriver
chrome_options = Options()
chrome_options.add_argument('headless')
chrome_options.add_argument('no-sandbox')
chrome_options.add_argument('disable-setuid-sandbox')
chrome_options.add_argument('window-size=1920,1200')
chrome_options.add_argument('ignore-certificate-errors')
chrome_options.add_argument('allow-running-insecure-content')
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('disable-gpu')
chrome_options.add_argument('disable-extensions')
chrome_options.add_argument('disable-dev-shm-usage')

service = Service('/usr/local/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)



driver.maximize_window()

driver.get("https://www.google.com")


assert "Example Domain" in driver.title
#Va a fallar en esta line 35 assert "Example Domain" in driver.title pero el entorno
#guarda bien el chromedriver lo llama actualiza bien el chrome stable el python reconoce el selenium asi que un exito


element = driver.find_element_by_name("q")
element.clear()
element.send_keys("Pruebas de automatización con Selenium")

button = driver.find_element_by_name("btnK")
button.click()

assert "No se encontraron resultados" not in driver.page_source

driver.quit()
