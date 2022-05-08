from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class LinkHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Link Should Be Present")
    def link_should_be_present(self, text, index="last()"):
        """
        Wait for link with exact ``text`` present in web page
         - uses ``(//a[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//a[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Link Should Not Be Present")
    def link_should_not_be_present(self, text, index="last()"):
        """
        Wait for link with exact ``text`` present in web page
         - uses ``(//a[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//a[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Link")
    def click_on_link(self, text, index="last()"):
        """
        Wait for link with exact ``text`` present in web page
         - uses ``(//a[normalize-space()='{text}'])[{index}]`` locator internally
        """
        locator = "(//a[normalize-space()='{text}'])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link With Retry")
    def click_on_link_with_retry(self, text, retry="3x", retry_interval="2s"):
        """
        Similar to `Click On Link` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Link", text)
    
    @keyword("Link By Text Should Be Present")
    def link_by_text_should_be_present(self, text, index="last()"):
        """
        Wait for link contains ``text`` present in web page
         - uses ``(//a[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Link By Text Should Not Be Present")
    def link_by_text_should_not_be_present(self, text, index="last()"):
        """
        Wait for link contains ``text`` not present in web page
         - uses ``(//a[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Link By Text")
    def click_on_link_by_text(self, text, index="last()"):
        """
        Wait for link contains ``text`` present in web page then scroll to element & perform click operation
         - uses ``(//a[contains(normalize-space(),'{text}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(),'{text}')])[{index}]".format(text=text, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link By Text With Retry")
    def click_on_link_by_text_with_retry(self, text, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On Link By Text` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Link By Text", text, index)
    
    @keyword("Link By Title Should Be Present")
    def link_by_title_should_be_present(self, title, index="last()"):
        """
        Wait for link with ``@title`` attribute contains value present in web page
         - uses ``(//a[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Link By Title Should Not Be Present")
    def link_by_title_should_not_be_present(self, title, index="last()"):
        """
        Wait for link with ``@title`` attribute contains value not present in web page
         - uses ``(//a[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element_not_present(self, self.sellib, locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Click On Link By Title")
    def click_on_link_by_title(self, title, index="last()"):
        """
        Wait for link with ``@title`` attribute contains value present in web page then scroll to element & perform click
         - uses ``(//a[contains(normalize-space(@title),'{title}')])[{index}]`` locator internally
        """
        locator = "(//a[contains(normalize-space(@title),'{title}')])[{index}]".format(title=title, index=index)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link By Title With Retry")
    def click_on_link_by_title_with_retry(self, title, index="last()", retry="3x", retry_interval="2s"):
        """
        Similar to `Click On Link By Title` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Click On Link By Title", title, index)