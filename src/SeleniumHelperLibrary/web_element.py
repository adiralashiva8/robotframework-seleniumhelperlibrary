from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class WebElementHelper(Util):

    def __init__(self):
        pass

    @keyword("WebElement By Text Should Be Present")
    def webelement_by_text_should_be_present(self, text, index="last()"):
        """
        Wait for webelement with exact `text` present in web page
         - uses ``(//*[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//*[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Text Should Not Be Present")
    def webelement_by_text_should_not_be_present(self, text, index="last()"):
        """
        Wait for webelement with exact `text` present in web page
         - uses ``(//*[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//*[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Text")
    def click_on_webelement_by_text(self, text, index="last()"):
        """
        Wait for webelement with exact `text` present in web page
         - uses ``(//*[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//*[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Text With Retry")
    def click_on_webelement_by_text_with_retry(self, text, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On WebElement` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Text", text, index)

    @keyword("WebElement With Text Should Be Present")
    def webelement_with_text_should_be_present(self, text, index="last()"):
        """
        Wait for webelement contains `text` present in web page
         - uses ``(//*[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement With Text Should Not Be Present")
    def webelement_with_text_should_not_be_present(self, text, index="last()"):
        """
        Wait for webelement contains `text` not present in web page
         - uses ``(//*[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement With Text")
    def click_on_webelement_with_text(self, text, index="last()"):
        """
        Wait for webelement contains `text` present in web page then scroll to element and perform click operation
         - uses ``(//*[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement With Text Retry")
    def click_on_webelement_with_text_retry(self, text, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On WebElement By Text` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement With Text", text, index)
    
    @keyword("WebElement By Title Should Be Present")
    def webelement_by_title_should_be_present(self, title, index="last()"):
        """
        Wait for webelement with ``@title`` attribute contains value present in web page
         - uses ``(//*[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Title Should Not Be Present")
    def webelement_by_title_should_not_be_present(self, title, index="last()"):
        """
        Wait for webelement with ``@title`` attribute contains value not present in web page
         - uses ``(//*[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Title")
    def click_on_webelement_by_title(self, title, index="last()"):
        """
        Wait for webelement with ``@title`` attribute contains value then scroll to element & perform click action on element in web page
         - uses ``(//*[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Title With Retry")
    def click_on_webelement_by_title_with_retry(self, title, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On WebElement By Title` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Title", title, index)
    
    @keyword("WebElement By Attribute Should Be Present")
    def webelement_by_attribute_should_be_present(self, attribute, value, index="last()"):
        """
        Wait for webelement with ``@attribute`` & ``value`` present in web page
         - uses ``(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]".format(attribute=attribute, value=value, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("WebElement By Attribute Should Not Be Present")
    def webelement_by_attribute_should_not_be_present(self, attribute, value, index="last()"):
        """
        Wait for webelement with ``@attribute`` & ``value`` not present in web page
         - uses ``(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]".format(attribute=attribute, value=value, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On WebElement By Attribute")
    def click_on_webelement_by_attribute(self, attribute, value, index="last()"):
        """
        Wait for webelement with ``@attribute`` & ``value`` present in web page then scroll to element & perform click operation
         - uses ``(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]`` locator internally
        """
        locator = "(//*[contains(normalize-space(@{attribute}),'{value}')])[{index}]".format(attribute=attribute, value=value, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On WebElement By Attribute With Retry")
    def click_on_webelement_by_attribute_with_retry(self, attribute, value, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On WebElement By Attribute` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On WebElement By Attribute", attribute, value, index)