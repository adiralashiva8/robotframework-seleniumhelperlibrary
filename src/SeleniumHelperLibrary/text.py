from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class TextHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Get WebElement Text")
    def get_webelement_text(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        value = None
        try:
            Util.wait_for_element(self, self.sellib, locator)
            value = self.sellib.get_text(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
        return value
    
    @keyword("Get WebElement Value")
    def get_webelement_value(self, locator, value):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        value = None
        try:
            Util.wait_for_element(self, self.sellib, locator)
            value = self.sellib.get_value(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
        return value