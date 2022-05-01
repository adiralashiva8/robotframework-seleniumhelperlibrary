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
        """
        Wait for button with ``text`` present in web page
         - uses ``//button[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Text Should Not Be Present")
    def button_by_text_should_not_be_present(self, text):
        """
        Waits for button with ``text`` not present in web page
         - uses ``//button[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Text")
    def click_on_button_by_text(self, text):
        """
        Waits for button with ``text`` and perform click action on button
         - uses ``//button[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Text With Retry")
    def click_on_button_by_text_with_retry(self, text, retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On Button By Text`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Text", text)
    
    @keyword("Button By Title Should Be Present")
    def button_by_title_should_be_present(self, title):
        """
        Wait for button with ``@title`` attribute value present in web page
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Button By Title Should Not Be Present")
    def button_by_title_should_not_be_present(self, title):
        """
        Wait for button with ``@title`` attribute value not present in web page
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Button By Title")
    def click_on_button_by_title(self, title):
        """
        Wait for button with ``@title`` attribute value and perform click action on button in web page
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//button[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Button By Title With Retry")
    def click_on_button_by_title_with_retry(self, title, retry="3x", retry_interval="2s"):
        """
        Similar to ``Click On Button By Title`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Button By Title", title)