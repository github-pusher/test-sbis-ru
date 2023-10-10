import logging

import re
import time

from pages.sbis_pages import SbisContactsPage
from pages.tenzor_pages import TenzorMainPage


def test_availability_of_elements(browser, log_path):
    logger = logging.getLogger('elements')

    logger.setLevel(logging.DEBUG)

    handler = logging.FileHandler(log_path)
    logger.addHandler(handler)

    logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
    logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)

    logger.info("Тест test_availability_of_elements запущен.")

    sbis_contacts_page = SbisContactsPage(browser)

    sbis_contacts_page.go_to_site()

    title = browser.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    logger.info("Браузер открыл нужную страницу.")

    browser.implicitly_wait(0.5)

    sbis_contacts_page.click_on_the_tenzor_logo()

    region_chooser_el = sbis_contacts_page.find_region_chooser_element()
    assert region_chooser_el.text != ""

    logger.info("Регион был выбран.")

    browser.implicitly_wait(0.5)

    browser.execute_script("arguments[0].click();", region_chooser_el)

    logger.info("Если тест провалится в первый раз на следующем шаге test_elements.py : 50 , перезапуск должен помочь.")

    browser.implicitly_wait(0.5)

    sbis_contacts_page.click_on_kamchatka_krai()

    time.sleep(3)

    url = browser.current_url
    assert url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"

    logger.info("Регион был успешно изменён на Камчатский край.")

    title = browser.title
    assert title == "СБИС Контакты — Камчатский край"

    logger.info("title страницы изменён в соответствии с изменением региона на Камчатский край.")

    tenzor_main_page = TenzorMainPage(browser)

    tenzor_main_page.go_to_site()

    browser.implicitly_wait(0.5)

    tenzor_main_page.click_on_more_details()

    for image in tenzor_main_page.find_all_images_in_we_are_working_element():
        assert image.get_attribute("height") == image.get_attribute("width")
        logger.info("У изображений в разделе «Мы работаем» одинаковые высота и ширина.")
