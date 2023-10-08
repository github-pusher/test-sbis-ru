import logging

import re
import time

from pages.sbis_pages import SbisContactsPage


def test_location_determination(browser, log_path):
    logger = logging.getLogger('location')

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)

    logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

    logger.info("Тест test_location_determination запущен.")

    sbis_contacts_page = SbisContactsPage(browser)

    sbis_contacts_page.go_to_site()

    title = browser.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    logger.info("Браузер открыл нужную страницу.")

    browser.implicitly_wait(0.5)

    region_chooser_el = sbis_contacts_page.find_region_chooser_element()
    assert region_chooser_el.text != ""

    logger.info("Регион был выбран.")

    browser.implicitly_wait(0.5)

    browser.execute_script("arguments[0].click();", region_chooser_el)

    time.sleep(3)

    logger.info("Если тест провалится в первый раз на следующем шаге test_location.py : 47 , перезапуск должен помочь.")

    sbis_contacts_page.click_on_kamchatka_krai()

    time.sleep(5)

    url = browser.current_url
    assert url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"

    logger.info("Регион был успешно изменён на Камчатский край.")

    title = browser.title
    assert title == "СБИС Контакты — Камчатский край"

    logger.info("title страницы изменён в соответствии с изменением региона на Камчатский край.")
