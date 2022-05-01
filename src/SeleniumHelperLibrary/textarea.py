from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class TextareaHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Textarea Field Value Should Be")
    def textarea_field_value_should_be(self, locator, text):
        """
        Wait for ``locator`` in webpage and validates given `text` present in textarea
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.textarea_value_should_be(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Textarea Field Value Should Contain")
    def textarea_field_value_should_contain(self, locator, text):
        """
        Wait for ``locator`` in webpage and validates given `text` contains in textarea
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.textarea_should_contain(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)