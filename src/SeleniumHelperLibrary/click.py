from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class ClickHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Click On WebElement")
    def click_on_webelement(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement With Retry")
    def click_on_webelement_with_retry(self, locator, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement", locator)
    
    @keyword("Click On WebElement If Exist")
    def click_on_webelement_if_exist(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            element_count = self.sellib.get_element_count(locator)
            if element_count > 0 :
                Util.wait_for_element(self, self.sellib, locator)
                self.sellib.click_element(locator)
            else:
                logger.info("No Action Performed: Element with locator {loc} count is: {count}".format(loc=locator, count=element_count))
        except Exception as e:
            Util.log_failure(self, self.sellib, e)