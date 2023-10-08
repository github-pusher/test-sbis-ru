import re
import time

from pages.sbis_pages import SbisContactsPage
from pages.tenzor_pages import TenzorMainPage


def test_availability_of_elements(browser):
    sbis_contacts_page = SbisContactsPage(browser)

    sbis_contacts_page.go_to_site()

    title = browser.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    browser.implicitly_wait(0.5)

    sbis_contacts_page.click_on_the_tenzor_logo()

    time.sleep(3)

    tenzor_main_page = TenzorMainPage(browser)

    tenzor_main_page.go_to_site()

    browser.implicitly_wait(0.5)

    tenzor_main_page.click_on_more_details()

    for image in tenzor_main_page.find_all_images_in_we_are_working_element():
        assert image.get_attribute("height") == image.get_attribute("width")
