from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class SelectHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Select Label From Picklist")
    def select_label_from_picklist(self, locator, label):
        """
        Wait for picklist with ``locator`` present in webpage then scroll to element & select option based on display text (label)
        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.select_from_list_by_label(locator, label)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Select Label From Picklist With Retry")
    def select_label_from_picklist_with_retry(self, locator, label, retry="3x", retry_interval="2s"):
        """
        Similar to `Select Label From Picklist` with retry
        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Select Label From Picklist", locator, label)