from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .click import ClickHelper
from .input import InputHelper

class SeleniumHelperLibrary(ClickHelper, InputHelper):

    """
    Core principal of helper library to achieve synchornization before performing any action on ``WebElement``

    Every ``Keyword`` consist following steps
        - Wait For WebElement
        - Scroll To WebElement (ignores scroll issues)
        - Perform Respective Action
    
    """

    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = VERSION

    def __init__(self):
        pass