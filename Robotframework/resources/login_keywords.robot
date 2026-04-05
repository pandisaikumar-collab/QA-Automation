*** Settings ***
Library    SeleniumLibrary
Library    JSONLibrary
Resource    ../locators/login_locators.robot
Library    ../utils/table_utils.py

*** Variables ***
${URL}    https://opensource-demo.orangehrmlive.com/
${BROWSER}    chrome
${TABLE_ROWS}    //div[@class='oxd-table-body']//div[@role='row']


*** Keywords ***
Launch The Website
    Open Browser    ${URL}    ${BROWSER}
    Sleep    10s

Enter Credentials
    Wait Until Page Contains Element    ${CREDENTIALS_AREA}
    Input Text    ${USERNAME}    Admin
    Input Text    ${PASSWORD}    admin123
    Click Button    ${LOGIN}
    Maximize Browser Window
    Sleep    5s

Admin Operations
    Click Element    ${ADMIN}
    Wait Until Page Contains Element    ${JOB}
    Click Element    ${JOB}
    Wait Until Element Is Visible    ${JOB_OPTIONS.format("Work Shifts")}
    Click Element    ${JOB_OPTIONS.format("Work Shifts")}
    Wait Until Element Is Visible    ${TABLE_ROWS}
    #Validate Work Shift Table

Validate Work Shift Table
    ${ui_data}=    Get Work Shift Table
    Log    UI Data: ${ui_data}
    ${expected}=    Load JSON From File    ${EXECDIR}/testdata/work_shifts.json
    Log    Expected Data: ${expected}
    Should Be Equal    ${ui_data}    ${expected}

Close The Browser
    Close All Browsers


    
