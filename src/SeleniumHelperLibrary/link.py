from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class LinkHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Click On Link By Text")
    def click_on_link_by_text(self, text):
        locator = "//a[contains(normalize-space(text(),'{text}'))]".format(text=text)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Click On Link By Title")
    def click_on_link_by_text(self, title):
        locator = "//a[contains(normalize-space(@title,'{title}'))]".format(title=title)
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.click_element(locator)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)