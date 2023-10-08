from selenium.webdriver.common.by import By

from pages.base_app import BasePage


class TenzorMainPageLocators:
    LOCATOR_POWER_IS_IN_PEOPLE = (By.CLASS_NAME, "tensor_ru-Index__block4-bg")
    LOCATOR_WE_ARE_WORKING = (By.CLASS_NAME, "tensor_ru-About__block3")


class TenzorMainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://tensor.ru")

    def click_on_more_details(self):
        more_details_el = self.find_element(TenzorMainPageLocators.LOCATOR_POWER_IS_IN_PEOPLE, time=2).find_element(
            by=By.CSS_SELECTOR, value="a")
        return self.driver.execute_script("arguments[0].click();", more_details_el)

    def find_all_images_in_we_are_working_element(self):
        return self.find_element(TenzorMainPageLocators.LOCATOR_WE_ARE_WORKING, time=2).find_elements(
            by=By.CLASS_NAME, value="tensor_ru-About__block3-image")
