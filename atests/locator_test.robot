*** Settings ***
Library          SeleniumLibrary
Library          SeleniumHelperLibrary
Resource         ${EXECDIR}/atests/setup.resource
Test Setup       Atest Test Setup
Test Teardown    Close All Browsers

*** Test Cases ***
Attribute Locator Test
    ${locator}=    Get Xpath With Attribute Value    input    id    firstName
    Wait Until Page Contains Element    ${locator}
    ${locator}=    Get Xpath With Attribute Contains Value   input    id    first
    Wait Until Page Contains Element    ${locator}

Xpath With Text Test Case
    ${locator}=    Get Xpath Contains Text    label    Mobile
    Wait Until Page Contains Element    ${locator}
    ${locator}=    Get Xpath With Text    label    Name
    Wait Until Page Contains Element    ${locator}