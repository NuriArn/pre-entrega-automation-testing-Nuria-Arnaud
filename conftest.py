import os
import datetime as dt
import logging
from logging.handlers import RotatingFileHandler

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager


# ---------- LOGGING ----------
def _setup_logger():
    os.makedirs("logs", exist_ok=True)
    logger = logging.getLogger("suite")
    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger  # evita duplicar handlers

    fh = RotatingFileHandler(
        "logs/suite.log",
        maxBytes=1_000_000,   # 1 MB
        backupCount=5,
        encoding="utf-8"
    )
    formatter = logging.Formatter("%(asctime)s | %(levelname)s | %(message)s")
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


LOGGER = _setup_logger()


# ---------- FIXTURES ----------

from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    chrome_opt = Options()
    #abre chrome como incognito y desactiva popup de
    #contraseña filtrada, que impedia que los test cases se ejecuten bien
    chrome_opt.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, 10)


# ---------- SCREENSHOTS ON FAIL ----------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Si falla un test UI, guarda screenshot en reports/screens/"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            os.makedirs("reports/screens", exist_ok=True)
            timestamp = dt.datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            path = os.path.join("reports/screens", file_name)
            driver.save_screenshot(path)
            LOGGER.info(f"Screenshot guardada: {path}")
