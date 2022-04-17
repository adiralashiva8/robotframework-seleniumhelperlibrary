from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .attribute import AttributeHelper
from .checkbox import CheckboxHelper
from .click import ClickHelper
from .frame import FrameHelper
from .input import InputHelper
from .select import SelectHelper
from .textarea import TextareaHelper
from .title import TitleHelper
from .wait import WaitHelper
from .xpath import XpathHelper
from .text import TextHelper
from .util import Util

class SeleniumHelperLibrary(AttributeHelper, CheckboxHelper, ClickHelper,
 FrameHelper, InputHelper, SelectHelper, TextareaHelper, TitleHelper, WaitHelper,
 XpathHelper, TextHelper):

    """
    Core principal of helper library to achieve synchronization before performing any action on ``WebElement``

    Every ``Keyword`` consist following steps
        - Wait For WebElement
        - Scroll To WebElement (ignores scroll issues)
        - Perform Respective Action
    
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        pass

    @keyword("Scroll By Coordinates")
    def scroll_by_coordinates(self, x, y):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        js = "window.scroll({x},{y})".format(x=x, y=y)
        self.sellib.execute_javascript(js)

    @keyword("Should Contain With Screenshot")
    def should_contain_with_screenshot(self, actual, expected):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        isPassed = BuiltIn().run_keyword_and_return_status("BuiltIn.Should Contain", actual, expected)
        if not isPassed:
            error_msg = "{expected_value} is not found in {actual_value}".format(expected_value=expected, actual_value=actual)
            Util.log_failure(self, self.sellib, error_msg)
    
    @keyword("Should Be Equal As Strings With Screenshot")
    def should_be_equal_as_strings_with_screenshot(self, actual, expected):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        isPassed = BuiltIn().run_keyword_and_return_status("BuiltIn.Should Be Equal As Strings", actual, expected)
        if not isPassed:
            error_msg = "{expected_value} is not same as {actual_value}".format(expected_value=expected, actual_value=actual)
            Util.log_failure(self, self.sellib, error_msg)

    @keyword("Reload Webpage")
    def reload_webpage(self):
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.sellib.reload_page()
        BuiltIn().run_keyword("SeleniumHelperLibrary.Wait Until DOM Loaded")