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
        """
        Wait for ``locator`` present in page then scroll to locator and perform click operation
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement With Retry")
    def click_on_webelement_with_retry(self, locator, retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On WebElement`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement", locator)