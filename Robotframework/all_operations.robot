*** Settings ***
Library    SeleniumLibrary


*** Variables ***
${URL}             https://opensource-demo.orangehrmlive.com/
${BROWSER}        chrome
${CREDENTIALS}      //div[contains(@class, 'credentials')]
${USERNAME}    //input[@name='username']
${PASSWORD}    //input[@name='password']
${LOGIN}    //button[contains(@class, 'login-button')]


*** Keywords ***
Launch Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    5s

Enter Credentials
    Wait Until Element Is Visible   ${CREDENTIALS}    timeout=10
    Input Text   ${USERNAME}     Admin
    Input Text   ${PASSWORD}     admin123
    Click Element   ${LOGIN}
    Sleep   5s

*** Test Cases ***
Test Using Keywords
    Launch Browser
    Enter Credentials