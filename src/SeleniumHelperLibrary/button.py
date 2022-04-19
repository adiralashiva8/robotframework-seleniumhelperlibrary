from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class ButtonHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Button By Text Should Be Present")
    def button_by_text_should_be_present(self, text):
        locator = "//button[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Text Should Not Be Present")
    def button_by_text_should_not_be_present(self, text):
        locator = "//button[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Text")
    def click_on_button_by_text(self, text):
        locator = "//button[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Text With Retry")
    def click_on_button_by_text_with_retry(self, text, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Text", text)
    
    @keyword("Button By Title Should Be Present")
    def button_by_title_should_be_present(self, title):
        locator = "//button[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Title Should Not Be Present")
    def button_by_title_should_not_be_present(self, title):
        locator = "//button[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Title")
    def click_on_button_by_title(self, title):
        locator = "//button[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Title With Retry")
    def click_on_button_by_title_with_retry(self, title, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Title", title)