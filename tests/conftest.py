import logging
import os
from datetime import datetime

import pytest
from selenium import webdriver


current_directory = os.getcwd()


@pytest.fixture(scope='session')
def browser():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()


@pytest.fixture(scope='function')
def log_path():
    suffix = datetime.now().strftime("%y%m%d_%H%M%S")
    log_path = f'{current_directory}\\logs\\log_file_{suffix}.log'

    yield log_path

    logger = logging.getLogger('selenium')
    for handler in logger.handlers:
        logger.removeHandler(handler)
        handler.close()
