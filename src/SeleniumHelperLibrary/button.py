from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class ButtonHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Button Should Be Present")
    def button_should_be_present(self, text, index="last()"):
        """
        Wait for button with exact ``text`` present in web page
         - uses ``(//button[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//button[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button Should Not Be Present")
    def button_should_not_be_present(self, text, index="last()"):
        """
        Wait for button with exact ``text`` not present in web page
         - uses ``(//button[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//button[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button")
    def click_on_button(self, text, index="last()"):
        """
        Wait for button with exact ``text`` present in web page then scroll to element and perform click
         - uses ``(//button[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//button[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button With Retry")
    def click_on_button_with_retry(self, text, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On Button`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button", text, index)
    
    @keyword("Button By Text Should Be Present")
    def button_by_text_should_be_present(self, text, index="last()"):
        """
        Wait for button contains ``text`` present in web page
         - uses ``(//button[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Text Should Not Be Present")
    def button_by_text_should_not_be_present(self, text, index="last()"):
        """
        Waits for button contains ``text`` not present in web page
         - uses ``(//button[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Text")
    def click_on_button_by_text(self, text, index="last()"):
        """
        Waits for button contains ``text`` and perform click action on button
         - uses ``(//button[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Text With Retry")
    def click_on_button_by_text_with_retry(self, text, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On Button By Text`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Text", text, index)
    
    @keyword("Button By Title Should Be Present")
    def button_by_title_should_be_present(self, title, index="last()"):
        """
        Wait for button with ``@title`` attribute contains value is present in web page
         - uses ``(//button[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Title Should Not Be Present")
    def button_by_title_should_not_be_present(self, title, index="last()"):
        """
        Wait for button with ``@title`` attribute contains value is not present in web page
         - uses ``(//button[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Title")
    def click_on_button_by_title(self, title, index="last()"):
        """
        Wait for button with ``@title`` attribute contains value and perform click action on button in web page
         - uses ``(//button[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//button[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Title With Retry")
    def click_on_button_by_title_with_retry(self, title, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On Button By Title`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Title", title, index)