import re

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_availability_of_elements():
    driver = webdriver.Chrome()

    driver.get("https://sbis.ru/contacts")

    title = driver.title
    match = re.search(r"СБИС Контакты — \D+", title)
    assert title == match[0]

    driver.implicitly_wait(0.5)

    tenzor_logo_el = driver.find_element(by=By.CLASS_NAME, value="sbisru-Contacts__logo-tensor")

    tenzor_logo_el.click()

    driver.get("https://tensor.ru")

    power_is_in_people_el = driver.find_element(by=By.CLASS_NAME, value="tensor_ru-Index__block4-bg")

    more_details_el = power_is_in_people_el.find_element(by=By.CSS_SELECTOR, value="a")

    driver.execute_script("arguments[0].click();", more_details_el)

    we_are_working_el = driver.find_element(by=By.CLASS_NAME, value="tensor_ru-About__block3")

    all_images_in_we_are_working_el = we_are_working_el.find_elements(by=By.CLASS_NAME, value="tensor_ru-About__block3-image")

    for image in all_images_in_we_are_working_el:
        assert image.get_attribute("height") == image.get_attribute("width")

    driver.quit()
