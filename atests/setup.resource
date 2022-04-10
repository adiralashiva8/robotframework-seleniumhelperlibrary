*** Settings ***
Library          SeleniumLibrary
Library          SeleniumHelperLibrary

*** Keywords ***
Atest Test Setup
    Open Browser   https://demoqa.com/automation-practice-form   Chrome
    Wait Until Dom Loaded
    Wait Until Page Contains With Retry    Student Registration Form

Navigate To WebPage
    [Arguments]    ${url}
    Go To    ${url}
    Wait Until Dom Loaded