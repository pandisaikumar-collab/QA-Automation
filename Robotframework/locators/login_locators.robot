*** Variables ***
${CREDENTIALS_AREA}    //div[contains(@class, 'credentials')]
${USERNAME}    //input[@name='username']
${PASSWORD}    //input[@name='password']
${LOGIN}    //button[contains(@class, 'login-button')]

${ADMIN}    //span[text()='Admin']
${JOB}    //span[text()='Job ']/i
${JOB_OPTIONS}    //span[text()='Job ']//..//ul[contains(@class, 'dropdown-menu')]/li[normalize-space()='{}']