import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from file_size_formatter import human_read_format


def test_download_success_and_downloaded_file_size():
    # Чтобы предотвратить диалог загрузки добавлены опции prefs
    options = webdriver.ChromeOptions()

    prefs = {
        "download.default_directory": "test-sbis-ru",
        "safebrowsing.enabled": True,
        "profile.default_content_settings.popups": 0,
    }

    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)

    driver.get("https://sbis.ru")

    download_sbis_el = driver.find_element(by=By.XPATH, value="//a[contains(text(),'Скачать СБИС')]")

    driver.execute_script("arguments[0].click();", download_sbis_el)

    time.sleep(3)

    download_plugin_el = driver.find_element(by=By.CSS_SELECTOR, value="div.controls-TabButtons>div:nth-child(2)")

    driver.execute_script("arguments[0].click();", download_plugin_el)

    time.sleep(1)

    if not os.path.exists("test-sbis-ru\\sbisplugin-setup-web.exe"):
        download_exe_3_64_mb_el = driver.find_element(by=By.XPATH, value="//a[contains(text(),'Скачать (Exe 3.64 МБ)')]")

        download_exe_3_64_mb_el.click()

        time.sleep(5)

    file_size = os.path.getsize("test-sbis-ru\\sbisplugin-setup-web.exe")

    assert human_read_format(file_size) == "3.64 МБ"

    driver.quit()
