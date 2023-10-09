import logging

import re

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

    tenzor_main_page = TenzorMainPage(browser)

    tenzor_main_page.go_to_site()

    browser.implicitly_wait(0.5)

    tenzor_main_page.click_on_more_details()

    for image in tenzor_main_page.find_all_images_in_we_are_working_element():
        assert image.get_attribute("height") == image.get_attribute("width")
        logger.info("У изображений в разделе «Мы работаем» одинаковые высота и ширина.")
