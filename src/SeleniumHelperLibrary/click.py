from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class ClickHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Click On WebElement")
    def click_on_webelement(self, locator):
        """
        Perform ``click`` action on ``WebElement``

        |  = Attribute =  |  = Description =  |
        | locator         |  WebElement to be clicked  |

        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)