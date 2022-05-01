from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class TitleHelper(Util):

    def __init__(self):
        pass

    @keyword("Title Should Contain")
    def title_should_contain(self, value):
        """
        Fetch current window title and compare title contains `value`
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            title = self.sellib.get_title()
            BuiltIn().should_contain(title, value)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)