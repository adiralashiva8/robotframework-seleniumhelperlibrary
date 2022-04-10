*** Settings ***
Library          SeleniumLibrary
Library          SeleniumHelperLibrary
Resource         ${EXECDIR}/atests/setup.resource
Test Setup       Atest Test Setup
Test Teardown    Close All Browsers

*** Test Cases ***
Attribute Test
    ${value}=    Get WebElement Attribute    class:header-wrapper    style
    Log   ${value}
    WebElement Attribute Should Contain    class:header-wrapper    style    rgb(108, 117, 125);

Checkbox Test
    Navigate To WebPage    https://demoqa.com/checkbox
    Select Checkbox Item      xpath://label[./span[text()='Home']]//span
    Unselect Checkbox Item    xpath://label[./span[text()='Home']]//span

Click Test
    ${locator}=    Get Xpath With Normalize Space Text    div    Elements
    Click On WebElement   ${locator}
    Click On WebElement If Exist   xpath://div[normalize-space()='Elements 123']
    Click On WebElement With Retry   xpath://div[normalize-space()='Elements Demo']

Frame Test
    Navigate To WebPage    https://demoqa.com/frames
    Switch To iFrame    id:frame1

Input Test    
    Input Text Into Textbox With Retry    name:q1    text
    Input Text Into Textbox    name:q    text
    Input Text Into Textbox If Exist    name:q    Exist

Select Test
    No Operation

TextArea Test
    Navigate To WebPage    https://demoqa.com/text-box
    Input Text Into Textbox    id:currentAddress    Hello World
    Textarea Field Value Should Be    id:currentAddress    Hello World
    Textarea Field Value Should Contain    id:currentAddress    World

Title Test
    Title Should Contain   Tools

Wait Test
    Navigate To WebPage    https://demoqa.com/dynamic-properties
    Wait For WebElement    id:visibleAfter
    Reload Webpage
    Wait Until Element Is Visible With Retry   id:visibleAfter
    Reload Webpage
    Wait Until Page Contains With Retry    Visible After 5 Seconds
    Reload Webpage
    Wait Until Page Contains Element With Retry   id:visibleAfter