import os
import pathlib
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from utils.logger_config import logger

SCREENSHOTS_DIR = pathlib.Path('reports/screens')
SCREENSHOTS_DIR.mkdir(parents=True, exist_ok=True)
BASE_URL = "https://www.saucedemo.com/"

def before_all(context):
    logger.info("Configurando WebDriver para toda la ejecucion")
    firefox_options = Options()
    if os.getenv("CI") == "true":
        firefox_options.add_argument("--headless")
    firefox_options.add_argument("--disable-dev-shm-usage")
    service = Service()
    context.driver = webdriver.Firefox(service=service, options=firefox_options)
    context.driver.maximize_window()
    context.driver.implicitly_wait(5)

def before_scenario(context, scenario):
    logger.info(f"Reseteando estado de la app antes de: {scenario.name}")
    context.driver.get(BASE_URL)
    context.driver.delete_all_cookies()
    context.driver.execute_script("window.localStorage.clear();")
    context.driver.execute_script("window.sessionStorage.clear();")

def after_step(context, step):
    if step.status == "failed":
        nombre_archivo = f"{context.feature.name}_{step.name}".replace(' ', '_').replace('"', '')
        file_name = SCREENSHOTS_DIR / f"{nombre_archivo}.png"
        context.driver.save_screenshot(str(file_name))
        logger.info(f"Screenshot guardado por fallo en: {file_name}")

def after_all(context):
    logger.info("Cerrando WebDriver, fin de la ejecucion")
    context.driver.quit()