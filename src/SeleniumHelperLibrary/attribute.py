from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class AttributeHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Get WebElement Attribute")
    def get_webelement_attribute(self, locator, attribute):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        value = None
        try:
            Util.wait_for_element(self, self.sellib, locator)
            value = self.sellib.get_element_attribute(locator, attribute)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
        return value
    
    @keyword("WebElement Attribute Should Contain")
    def webelement_attribute_should_contain(self, locator, attribute, value):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            actual = self.sellib.get_element_attribute(locator, attribute)
            BuiltIn().should_contain(actual, value)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)