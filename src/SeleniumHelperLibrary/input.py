from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class InputHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Input Text Into Textbox")
    def input_text_into_textbox(self, locator, text, clear=True):
        """
        Input text into ``locator`` textbox

        |  = Attribute =  |  = Description =  |
        | locator         |  texbox locator  |
        | text            |  value to be entered in textbox  |
        | clear           |  clear textbox before enter text |

        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.input_text(locator, text, clear)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
    
    @keyword("Input Text Into Textbox If Exist")
    def input_text_into_textbox_if_exist(self, locator, text, clear=True):
        """
        Input text into ``locator`` textbox if ``locator`` present in webpage.
         - First it fetch ``WebElement`` count
         - verifies if __count__ greater than zero
         - if count > 0 performs actions

        |  = Attribute =  |  = Description =  |
        | locator         |  texbox locator  |
        | text            |  value to be entered in textbox  |
        | clear           |  clear textbox before enter text |

        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            element_count = self.sellib.get_element_count(locator)
            if element_count > 0 :
                Util.wait_for_element(self, self.sellib, locator)
                self.sellib.input_text(locator, text, clear)
            else:
                logger.info("No Action Performed: Element with locator {loc} count is: {count}".format(loc=locator, count=element_count))
        except Exception as e:
            Util.log_failure(self, self.sellib, e)

    @keyword("Input Text Into Textbox Using Javascript")
    def input_text_into_textbox_using_javascript(self, locator, text):
        """
        Input text into ``locator`` textbox using javascript

        |  = Attribute =  |  = Description =  |
        | locator         |  texbox locator  |
        | text            |  value to be entered in textbox  |

        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            webelement = """document.evaluate("{locator}", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue""".format(locator=locator)
            js = """{element}.value='{value}'""".format(element=webelement, value=text)
            self.sellib.execute_javascript(js)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)
        
    @keyword("Input Text Into Textbox With Retry")
    def input_text_into_textbox_with_retry(self, locator, text, retry="3x", retry_interval="2s", clear=True):
        """
        Input text into ``locator`` textbox using retry

        |  = Attribute =  |  = Description =  |
        | locator         |  texbox locator  |
        | text            |  value to be entered in textbox  |
        | retry           |  retry times  |
        | retry_interval  |  time to wait _after_ a keyword has failed  |
        | clear           |  clear textbox before enter text |

        """
        BuiltIn().wait_until_keyword_succeeds(retry, retry_interval, "SeleniumHelperLibrary.Input Text Into Textbox", locator, text, clear)
    
    @keyword("Textbox Should Contain Value")
    def textbox_should_contain_value(self, locator, text):
        """
        Validates textbox contains ``text``

        |  = Attribute =  |  = Description =  |
        | locator         |  WebElement to be clicked  |
        | text            |  textbox should contain value  |

        """
        self.sellib = BuiltIn().get_library_instance('SeleniumLibrary')
        try:
            Util.wait_for_element(self, self.sellib, locator)
            self.sellib.textfield_should_contain(locator, text)
        except Exception as e:
            Util.log_failure(self, self.sellib, e)