from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, host, address_part=""):
        self.driver = driver
        self.base_url = f"{host}/{address_part}"

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Не могу найти эллемент по локатору {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Не могу найти эллемент по локатору {locator}")

    def go_to_site(self):
        return self.driver.get(self.base_url)
