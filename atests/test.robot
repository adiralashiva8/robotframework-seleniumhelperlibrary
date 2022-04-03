*** Settings ***
Library          SeleniumLibrary
Library          SeleniumHelperLibrary
Test Setup       Atest Test Setup
Test Teardown    Close All Browsers

*** Test Cases ***
Attribute Test
    ${value}=    Get WebElement Attribute    class:header-wrapper    style
    Log   ${value}
    WebElement Attribute Should Contain    class:header-wrapper    style    rgb(108, 117, 125);

Checkbox Test
    Select Checkbox Item      xpath://div[./label[text()='Sports']]//input
    Unselect Checkbox Item    xpath://div[./label[text()='Sports']]//input

Click Test
    No Operation

Frame Test
    No Operation

Input Test    
    Input Text Into Textbox With Retry    name:q1    text
    Input Text Into Textbox    name:q    text
    Input Text Into Textbox If Exist    name:q    Exist

Select Test
    No Operation

TextArea Test
    No Operation

Title Test
    No Operation

Wait Test
    No Operation

*** Keywords ***
Atest Test Setup
    Open Browser   https://demoqa.com/automation-practice-form   Chrome
    Wait Until Page Contains With Retry    Student Registration Form