from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class CheckboxHelper(Util):

    def __init__(self):
        pass

    @keyword("Select Checkbox Item")
    def select_checkbox_item(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.select_checkbox(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Unselect Checkbox Item")
    def unselect_checkbox_item(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.unselect_checkbox(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)