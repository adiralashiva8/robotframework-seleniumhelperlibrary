from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class InputHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Input Text Into Textbox")
    def input_text_into_textbox(self, locator, text):
        """
        Wait for ``locator`` present in webpage then scroll to element and input text
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.input_text(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Input Text Into Textbox With Retry")
    def input_text_into_textbox_with_retry(self, locator, text, retry="3x", retry_interval="2s"):
        """
        Similar to ``Input Text Into Textbox`` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Input Text Into Textbox", locator, text)
    
    @keyword("Textbox Should Contain Value")
    def textbox_should_contain_value(self, locator, text):
        """
        Wait for ``locator`` then scroll to element & validates textbox `@value` attribute contains give `text`
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.textfield_should_contain(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)