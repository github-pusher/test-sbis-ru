from selenium.webdriver.common.by import By

from pages.base_app import BasePage


class TenzorMainPageLocators:
    LOCATOR_POWER_IS_IN_PEOPLE = (By.XPATH, "//div[@class='tensor_ru-Index__block4-content tensor_ru-Index__card']")
    LOCATOR_WE_ARE_WORKING = (By.XPATH, "//div[@class='tensor_ru-container tensor_ru-section tensor_ru-About__block3']")


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
