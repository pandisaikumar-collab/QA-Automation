*** Settings ***
Resource    ../resources/home_keywords.robot

*** Test Cases ***
Verify Users Can Navigate To Elements Section
    [Documentation]    Opens DemoQA and clicks the Element card.
    Open DemoQA Website
    Click On Elements Card
