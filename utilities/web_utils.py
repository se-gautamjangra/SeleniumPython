from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.common.action_chains import ActionChains
from traceback import print_stack


class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            print('Locator type not supported - ' + locator_type)
            return False

    def get_element(self, locator, locator_type='id'):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            self.wait_for_element_presence(locator, locator_type)
            element = self.driver.find_element(by_type, locator)
            print('element found  with ' + locator_type + '- ' + locator)
        except:
            print('element not found  with ' + locator_type + '- ' + locator)
        return element

    def get_elements(self, locator, locator_type='id'):
        elements = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            self.wait_for_element_presence(locator, locator_type)
            elements = self.driver.find_elements(by_type, locator)
            print('elements found  with ' + locator_type + '- ' + locator)
        except:
            print('element not found  with ' + locator_type + '- ' + locator)
        return elements

    def click_element(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
            print('element clicked  with' + locator_type + '- ' + locator)
        except:
            print('unable to click element  with' + locator_type + '- ' + locator)
            print_stack()

    def set_text(self, data, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            element.clear()
            element.send_keys(data)
            print('text entered in element  with' + locator_type + '- ' + locator)
        except:
            print('element not found  with' + locator_type + '- ' + locator)
            print_stack()

    def is_element_present(self, locator, locator_type='id'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                print('element present  with' + locator_type + '- ' + locator)
                return True
            else:
                print('element not present  with' + locator_type + '- ' + locator)
                return False
        except:
            print('element not found  with' + locator_type + '- ' + locator)
            print_stack()

    def wait_for_element(self, locator, locator_type='id', timeout=10):
        element = None
        try:
            byType = self.getByType(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType,
                                                             "stopFilter_stops-0")))
            self.log.info("Element appeared on the web page")
        except:
            self.log.info("Element not appeared on the web page")
            print_stack()
        return element

    def wait_for_element_presence(self, locator, locator_type='id', timeout=10):
        by_type = self.get_by_type(locator_type)
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by_type, locator)))

    def scroll_to_element_view(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def perform_hover(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        hover_element = ActionChains(self.driver).move_to_element(element)
        hover_element.perform()

    def javascript_click(self, locator, locator_type='id'):
        element = self.get_element(locator, locator_type)
        self.driver.execute_script("arguments[0].click();", element)