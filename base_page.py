import datetime
import logging
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://test-stand.gb.ru'

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                         message=f"Can't find element by locator {locator}")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, property):
        element = self.find_element(locator)
        if element:
            return element.value_of_css_property(property)
        else:
            logging.error(f"Property {property} not found in element with locator{locator}")
            return None

    def go_to_site(self):
        try:
            start_browser = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open site")
            start_browser = None
        return start_browser

    def screenshot(self):
        try:
            now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
            name_screenshot = f"screenshot_{now_date}.png"
            self.driver.save_screenshot(name_screenshot)
        except:
            logging.exception("Exception while save screenshot")
            return None
