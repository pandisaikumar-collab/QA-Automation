*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Variables ***
${URL}             https://opensource-demo.orangehrmlive.com/
${PIM_URL}      https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList
${BROWSER}        edge
${CREDENTIALS}      //div[contains(@class, 'credentials')]
${USERNAME}    //input[@name='username']
${PASSWORD}    //input[@name='password']
${LOGIN}    //button[contains(@class, 'login-button')]
${ADMIN_SECTION}    //ul[contains(@class, 'oxd-main-menu')]//*[text()='Admin']
${SYSTEM_USERNAME}     //label[text()='Username']//ancestor::div[contains(@class, 'label-wrapper')]//..//input[contains(@class, 'input')]
${USER_ROLE}    //label[text()='User Role']
${RECORDS_FOUND}    //span[contains(.,'Records Found')]
${RECORD_FOUND_TABLE}    //div[@class='orangehrm-container']/div[@role='table']
${RECORD_CHECKBOX}      (//span[contains(.,'Records Found')]//following::div[@role='columnheader' and text()='Username']//..//span)[1]


*** Keywords ***
Launch Browser
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Sleep    15s

Enter Credentials
    Wait Until Element Is Visible   ${CREDENTIALS}    timeout=10
    Input Text   ${USERNAME}     Admin
    Input Text   ${PASSWORD}     admin123
    Click Element   ${LOGIN}
    Sleep   5s

Browser And Navigation
    Go To       ${PIM_URL}
    Sleep   2s
    Reload Page
    Sleep   3s
    Go Back
    Maximize Browser Window
    Sleep   3s

Element Actions
    Click Element       ${ADMIN_SECTION}
    Sleep   3s
    Input Text      ${SYSTEM_USERNAME}     Saikumar
    Sleep   2s
    Clear Element Text      ${SYSTEM_USERNAME}
    Sleep    2s

Wait Operations
    Wait Until Element Is Visible      ${USER_ROLE}    timeout=10
    Wait Until Element Is Enabled      ${SYSTEM_USERNAME}  timeout=10


Get Fetch Data
    ${record_text}=    Get Text    ${RECORDS_FOUND}
    Log    The text is: ${record_text}
    ${type}=    Evaluate    type($record_text)
    Log    ${type}

Get Fetch Data Multiple
    @{elements}=    Get Webelements    ${RECORD_FOUND_TABLE}
    @{all_texts}=    Create List
    FOR    ${element}    IN    @{elements}
        ${text}=    Get Text    ${element}
        Append To List    ${all_texts}    ${text}
    END
    Log Many    @{all_texts}

Handling Checkboxes
    Scroll Element Into View    ${RECORD_CHECKBOX}
    Sleep    10s
    Select Checkbox     ${RECORD_CHECKBOX}
    Sleep   2s
    Unselect Checkbox   ${RECORD_CHECKBOX}
    Sleep    2s


##<Testcases>
*** Test Cases ***
Test Using Keywords
    Launch Browser
    Enter Credentials
    Browser And Navigation
    Element Actions
    Wait Operations
    Get Fetch Data
    Get Fetch Data Multiple
    #Handling Checkboxes



























