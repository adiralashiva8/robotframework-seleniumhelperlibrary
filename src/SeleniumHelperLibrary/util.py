from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword, not_keyword
from robot.api import logger

class Util():

    def __init__(self):
        pass

    @not_keyword
    def wait_for_element(self, instance, locator):
        instance.wait_until_page_contains_element(locator)
        try:
            instance.scroll_element_into_view(locator)
        except:
            pass
    
    @not_keyword
    def wait_for_element_not_present(self, instance, locator):
        instance.wait_until_page_does_not_contain_element(locator)

    @not_keyword
    def log_failure(self, instance, exception):
        instance.capture_page_screenshot()
        BuiltIn().fail(exception)