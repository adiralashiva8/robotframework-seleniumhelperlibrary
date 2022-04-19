from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class WebElementHelper(Util):

    def __init__(self):
        pass
    
    @keyword("WebElement By Text Should Be Present")
    def webelement_by_text_should_be_present(self, text):
        locator = "//*[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Text Should Not Be Present")
    def webelement_by_text_should_not_be_present(self, text):
        locator = "//*[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Text")
    def click_on_webelement_by_text(self, text):
        locator = "//*[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Text With Retry")
    def click_on_webelement_by_text_with_retry(self, text, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Text", text)
    
    @keyword("WebElement By Title Should Be Present")
    def webelement_by_title_should_be_present(self, title):
        locator = "//*[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Title Should Not Be Present")
    def webelement_by_title_should_not_be_present(self, title):
        locator = "//*[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Title")
    def click_on_webelement_by_title(self, title):
        locator = "//*[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Title With Retry")
    def click_on_webelement_by_title_with_retry(self, title, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Title", title)
    
    @keyword("WebElement By Attribute Should Be Present")
    def webelement_by_attribute_should_be_present(self, attribute, value):
        locator = "//*[contains(normalize-space(@{attribute},'{value}'))]".format(attribute=attribute, value=value)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Attribute Should Not Be Present")
    def webelement_by_attribute_should_not_be_present(self, attribute, value):
        locator = "//*[contains(normalize-space(@{attribute},'{value}'))]".format(attribute=attribute, value=value)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Attribute")
    def click_on_webelement_by_attribute(self, attribute, value):
        locator = "//*[contains(normalize-space(@{attribute},'{value}'))]".format(attribute=attribute, value=value)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Attribute With Retry")
    def click_on_webelement_by_attribute_with_retry(self, attribute, value, retry="3x", retry_interval="2s"):
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Attribute", attribute, value)