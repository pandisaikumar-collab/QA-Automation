*** Settings ***
Resource    ../resources/login_keywords.robot

*** Test Cases ***
Launch The Website
    [Documentation]    Open the browser and Launch the website
    Launch The Website
    Enter Credentials
    Admin Operations
    Validate Work Shift Table
    Close The Browser