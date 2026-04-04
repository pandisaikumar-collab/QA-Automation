*** Settings ***
Library    SeleniumLibrary
Resource   ../locators/elements_locators.robot

*** Variables ***
${URL}    https://demoqa.com/
${BROWSER}    chrome

*** Keywords ***
Open DemoQA Website
    Open Browser                             ${URL}    ${BROWSER}
    Sleep                                    10s
    Maximize Browser Window
    Wait Until Element Is Visible            ${ALL_HOME_CARDS}    timeout=20

Click On Elements Card
    Execute Javascript                       window.scrollTo(0, 400)
    Wait Until Element Is Enabled            ${ELEMENTS_CARD}
    Click Element                            ${ELEMENTS_CARD}

