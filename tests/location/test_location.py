import re
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_location_determination():
    driver = webdriver.Chrome()

    driver.get("https://sbis.ru/contacts")

    title = driver.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    driver.implicitly_wait(0.5)

    region_chooser_el = driver.find_element(by=By.CLASS_NAME, value="sbis_ru-Region-Chooser__text")
    assert region_chooser_el.text != ""

    driver.implicitly_wait(0.5)

    region_chooser_el.click()

    time.sleep(3)

    kamchatka_krai_el = driver.find_element(by=By.XPATH, value="//span[contains(text(),'41 Камчатский край')]")

    kamchatka_krai_el.click()

    time.sleep(5)

    url = driver.current_url
    assert url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"

    title = driver.title
    assert title == "СБИС Контакты — Камчатский край"

    driver.quit()
