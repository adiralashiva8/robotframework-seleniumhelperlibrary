from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class WaitHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Wait Until Element Is Visible With Retry")
    def wait_until_element_is_visible_with_retry(self, locator, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumLibrary.Wait Until Element Is Visible", locator)
    
    @keyword("Wait Until Page Contains With Retry")
    def wait_until_page_contains_with_retry(self, text, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumLibrary.Wait Until Page Contains", text)
    
    @keyword("Wait Until Page Contains Element With Retry")
    def wait_until_page_contains_element_with_retry(self, locator, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumLibrary.Wait Until Page Contains Element", locator)
    
    @keyword("Wait For WebElement")
    def wait_for_webelement(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Wait Until DOM Loaded")
    def wait_until_dom_loaded(self):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            self.sellib.wait_for_condition('return window.document.readyState === "complete"')
        except Exception as e:
            Util.log_failure(self, self.sellib, e)