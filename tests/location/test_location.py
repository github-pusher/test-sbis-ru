import re
import time

from pages.sbis_pages import SbisContactsPage


def test_location_determination(browser):
    sbis_contacts_page = SbisContactsPage(browser)

    sbis_contacts_page.go_to_site()

    title = browser.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    browser.implicitly_wait(0.5)

    region_chooser_el = sbis_contacts_page.find_region_chooser_element()
    assert region_chooser_el.text != ""

    browser.implicitly_wait(0.5)

    browser.execute_script("arguments[0].click();", region_chooser_el)

    time.sleep(3)

    sbis_contacts_page.click_on_kamchatka_krai()

    time.sleep(5)

    url = browser.current_url
    assert url == "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"

    title = browser.title
    assert title == "СБИС Контакты — Камчатский край"
