*** Settings ***
Library    SeleniumLibrary
Library    SeleniumHelperLibrary

*** Test Cases ***
Google Accessibility Test
    Open Browser    https://www.google.com/    Chrome
    Input Text Into Textbox With Retry    name:q1    text
    Input Text Into Textbox    name:q    text
    Input Text Into Textbox If Exist    name:q    Exist
    # Input Text Into Textbox Using Javascript    name:q    Javscript
    Click On WebElement    xpath://a[text()='Gmail']
    [Teardown]    Close All Browsers