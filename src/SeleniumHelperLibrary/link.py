from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class LinkHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Link By Text Should Be Present")
    def link_by_text_should_be_present(self, text):
        """
        Wait for link with ``text`` present in web page
         - uses ``//a[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Link By Text Should Not Be Present")
    def link_by_text_should_not_be_present(self, text):
        """
        Wait for link with ``text`` not present in web page
         - uses ``//a[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Link By Text")
    def click_on_link_by_text(self, text):
        """
        Wait for link with ``text`` present in web page then scroll to element & perform click operation
         - uses ``//a[contains(normalize-space(text()),'{text}')]`` locator internally
         - ``text`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(text()),'{text}')]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link By Text With Retry")
    def click_on_link_by_text_with_retry(self, text, retry="3x", retry_interval="2s"):
        """
        Similar to `Click On Link By Text` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Link By Text", text)
    
    @keyword("Link By Title Should Be Present")
    def link_by_title_should_be_present(self, title):
        """
        Wait for link with ``@title`` attribute value present in web page
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Link By Title Should Not Be Present")
    def link_by_title_should_not_be_present(self, title):
        """
        Wait for link with ``@title`` attribute value not present in web page
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Link By Title")
    def click_on_link_by_title(self, title):
        """
        Wait for link with ``@title`` attribute value present in web page then scroll to element & perform click
         - uses ``//button[contains(normalize-space(@title),'{title}')]`` locator internally
         - ``title`` will be replaced in locator
        """
        locator = "//a[contains(normalize-space(@title),'{title}')]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link By Title With Retry")
    def click_on_link_by_title_with_retry(self, title, retry="3x", retry_interval="2s"):
        """
        Similar to `Click On Link By Title` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Link By Title", title)