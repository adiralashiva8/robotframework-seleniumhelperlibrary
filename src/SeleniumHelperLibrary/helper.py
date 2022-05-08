from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .attribute import AttributeHelper
from .click import ClickHelper
from .frame import FrameHelper
from .input import InputHelper
from .select import SelectHelper
from .textarea import TextareaHelper
from .title import TitleHelper
from .wait import WaitHelper
from .text import TextHelper
from .link import LinkHelper
from .button import ButtonHelper
from .web_element import WebElementHelper
from .util import Util

class SeleniumHelperLibrary(AttributeHelper, ClickHelper,
 FrameHelper, InputHelper, SelectHelper, TextareaHelper, TitleHelper, WaitHelper,
 LinkHelper, ButtonHelper, WebElementHelper, TextHelper):

    """
    Core Principal:
      Achieve synchronization before performing any action on ``WebElement``

    Every ``Keyword`` consist following steps
        - Wait For WebElement
        - Scroll To WebElement (ignores scroll issue)
        - Perform Respective Action
    
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        pass

    @keyword("Scroll By Coordinates")
    def scroll_by_coordinates(self, x, y):
        """
        Perform scroll in webpage based on co-ordinates
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        js = "window.scroll({x},{y})".format(x=x, y=y)
        self.sellib.execute_javascript(js)

    @keyword("Should Contain With Screenshot")
    def should_contain_with_screenshot(self, actual, expected):
        """
        Validates `actual` contains `expected` value.
         - Captures screenshot if failed
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        isPassed = BuiltIn().run_keyword_and_return_status("BuiltIn.Should Contain", actual, expected)
        if not isPassed:
            error_msg = "{expected_value} is not found in {actual_value}".format(expected_value=expected, actual_value=actual)
            Util.log_failure(self, self.sellib, error_msg)
    
    @keyword("Should Not Contain With Screenshot")
    def should_not_contain_with_screenshot(self, actual, expected):
        """
        Validates `actual` not contains `expected` value.
         - Captures screenshot if failed
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        isPassed = BuiltIn().run_keyword_and_return_status("BuiltIn.Should Not Contain", actual, expected)
        if not isPassed:
            error_msg = "{expected_value} is not found in {actual_value}".format(expected_value=expected, actual_value=actual)
            Util.log_failure(self, self.sellib, error_msg)
    
    @keyword("Should Be Equal As Strings With Screenshot")
    def should_be_equal_as_strings_with_screenshot(self, actual, expected):
        """
        Validates `actual` equals `expected` value.
         - Captures screenshot if failed
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        isPassed = BuiltIn().run_keyword_and_return_status("BuiltIn.Should Be Equal As Strings", actual, expected)
        if not isPassed:
            error_msg = "{expected_value} is not same as {actual_value}".format(expected_value=expected, actual_value=actual)
            Util.log_failure(self, self.sellib, error_msg)

    @keyword("Reload Webpage")
    def reload_webpage(self):
        """
        Performs reload in webpage and waits until dom get loaded
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        self.sellib.reload_page()
        BuiltIn().run_keyword("SeleniumHelperLibrary.Wait Until DOM Loaded")