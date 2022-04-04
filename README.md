# robotframework-seleniumhelper
Helper keywords for robotframework-selenium

[![PyPI version](https://badge.fury.io/py/robotframework-seleniumhelperlibrary.svg)](https://badge.fury.io/py/robotframework-seleniumhelperlibrary)
[![Downloads](https://pepy.tech/badge/robotframework-seleniumhelperlibrary)](https://pepy.tech/project/robotframework-seleniumhelperlibrary)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Core Prinicpal
Achieve synchornization before performing any action on ``WebElement``

    Every Helper Keyword consist following steps:
        - Wait For Page Contains WebElement
        - Scroll To WebElement (ignore error if any issues while scroll)
        - Perform Respective Action

# Installation:
To install robotframework-seleniumhelper
```
$ pip install robotframework-seleniumhelperlibrary
```

Install latest changes (master)
```
$ pip install git+https://github.com/adiralashiva8/robotframework-seleniumhelper
```

# Keyword Documentation
Keyword documentation [link]()

# Usage
```
*** Settings ***
Library    SeleniumLibrary
Library    SeleniumHelperLibrary

*** Test Cases ***
Selenium Helper Sample
    Open Browser    https://www.google.com/    Chrome
    Input Text Into Textbox    name:q    mytext
    Input Text Into Textbox If Exist    name:q    Exist
    Click On WebElement    xpath://a[text()='Gmail']
    # fail scenario
    Input Text Into Textbox With Retry    name:q1    text
    [Teardown]    Close All Browsers
```
---

If you have any questions / suggestions / comments on this, please feel free to reach me at

 - Email: <a href="mailto:adiralashiva8@gmail.com?Subject=Robotframework%20SeleniumHelper" target="_blank">`adiralashiva8@gmail.com`</a> 

---

:star: repo if you like it

---