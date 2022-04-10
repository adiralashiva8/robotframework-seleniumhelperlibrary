from .version import VERSION
from robot.libraries.BuiltIn import BuiltIn
from robot.api.deco import keyword
from robot.api import logger
from .util import Util

class XpathHelper(Util):

    def __init__(self):
        pass
    
    @keyword("Get Xpath With Text")
    def get_xpath_with_text(self, tag, text, index=1):
        xpath = "xpath:(//{TAG}[text()='{TEXT}'])[{INDEX}]"
        return xpath.format(TAG=tag, TEXT=text, INDEX=index)
    
    @keyword("Get Xpath Contains Text")
    def get_xpath_contains_text(self, tag, text, index=1):
        xpath = "xpath:(//{TAG}[contains(text(),'{TEXT}')])[{INDEX}]"
        return xpath.format(TAG=tag, TEXT=text, INDEX=index)
    
    @keyword("Get Xpath With Normalize Space Text")
    def get_xpath_with_normalize_space_text(self, tag, text, index=1):
        xpath = "xpath:(//{TAG}[normalize-space()='{TEXT}'])[{INDEX}]"
        return xpath.format(TAG=tag, TEXT=text, INDEX=index)
    
    @keyword("Get Xpath With Attribute Value")
    def get_xpath_with_attribute_value(self, tag, attribute, value, index=1):
        xpath = "xpath:(//{TAG}[@{ATTRIBUTE}='{VALUE}'])[{INDEX}]"
        return xpath.format(TAG=tag, ATTRIBUTE=attribute, VALUE=value, INDEX=index)
    
    @keyword("Get Xpath With Attribute Contains Value")
    def get_xpath_with_attribute_contains_value(self, tag, attribute, value, index=1):
        xpath = "xpath:(//{TAG}[contains(@{ATTRIBUTE},'{VALUE}')])[{INDEX}]"
        return xpath.format(TAG=tag, ATTRIBUTE=attribute, VALUE=value, INDEX=index)