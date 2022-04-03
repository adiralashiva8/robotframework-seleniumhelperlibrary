from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class FrameHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Switch To Iframe")
    def switch_to_iframe(self, locator):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.select_frame(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
