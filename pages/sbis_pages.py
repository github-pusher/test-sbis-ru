from selenium.webdriver.common.by import By

from pages.base_app import BasePage


class SbisContactsPageLocators:
    LOCATOR_TENZOR_LOGO = (By.XPATH, "//a[@class='sbisru-Contacts__logo-tensor mb-12']")
    LOCATOR_REGION_CHOOSER = (By.XPATH, "//span[@class='sbis_ru-Region-Chooser ml-16 ml-xm-0']//span[@class='sbis_ru-Region-Chooser__text sbis_ru-link']")
    LOCATOR_KAMCHATKA_KRAI = (By.XPATH, "//span[contains(text(),'41 Камчатский край')]")
    LOCATOR_DOWNLOAD_SBIS = (By.XPATH, "//a[contains(text(),'Скачать СБИС')]")
    LOCATOR_DOWNLOAD_PLUGIN = (By.CSS_SELECTOR, "div.controls-TabButtons>div:nth-child(2)")
    LOCATOR_DOWNLOAD_EXE_3_64_MB = (By.XPATH, "//a[contains(text(),'Скачать (Exe 3.64 МБ)')]")


class SbisMainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://sbis.ru")

    def click_on_download_sbis(self):
        download_sbis_el = self.find_element(SbisContactsPageLocators.LOCATOR_DOWNLOAD_SBIS, time=2)
        return self.driver.execute_script("arguments[0].click();", download_sbis_el)

    def click_on_download_plugin(self):
        download_plugin_el = self.find_element(SbisContactsPageLocators.LOCATOR_DOWNLOAD_PLUGIN, time=2)
        return self.driver.execute_script("arguments[0].click();", download_plugin_el)

    def click_on_download_exe_3_64_mb(self):
        return self.find_element(SbisContactsPageLocators.LOCATOR_DOWNLOAD_EXE_3_64_MB, time=2).click()


class SbisContactsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver, "https://sbis.ru", "contacts")

    def click_on_the_tenzor_logo(self):
        return self.find_element(SbisContactsPageLocators.LOCATOR_TENZOR_LOGO, time=2).click()  # надёжный метод

    def find_region_chooser_element(self):
        return self.find_element(SbisContactsPageLocators.LOCATOR_REGION_CHOOSER, time=2)

    def click_on_kamchatka_krai(self):
        return self.find_element(SbisContactsPageLocators.LOCATOR_KAMCHATKA_KRAI, time=20).click()
