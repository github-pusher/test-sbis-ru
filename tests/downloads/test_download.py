import logging

import os
import time

from selenium import webdriver

from tests.downloads.file_size_formatter import human_read_format

from pages.sbis_pages import SbisMainPage


current_directory = os.getcwd()


def test_download_success_and_downloaded_file_size(log_path):
    logger = logging.getLogger('downloads')

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)

    logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

    logger.info("Тест test_download_success_and_downloaded_file_size запущен.")

    # Чтобы предотвратить диалог загрузки добавлены опции prefs
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": current_directory,
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)

    sbis_main_page = SbisMainPage(driver)

    sbis_main_page.go_to_site()

    sbis_main_page.click_on_download_sbis()

    time.sleep(3)

    sbis_main_page.click_on_download_plugin()

    time.sleep(1)

    if not os.path.exists(f"{current_directory}\\sbisplugin-setup-web.exe"):
        sbis_main_page.click_on_download_exe_3_64_mb()

        time.sleep(10)

    file_size = os.path.getsize(f"{current_directory}\\sbisplugin-setup-web.exe")

    assert human_read_format(file_size) == "3.64 МБ"
    logger.info("Размер файла соответствует указанному на сайте — 3.64 МБ")
