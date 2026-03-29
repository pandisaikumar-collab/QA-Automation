"""
STLC: 

1) basically we have to test whether software application is working as expected. 
2) Need to verify and reporting on bugs. 

7 Phases of STLC:
=================
1) Requirement Analysis  
2) Test Planning  
3) Test Design  
4) Test Environment Setup  
5) Test Execution  
6) Defect Tracking  
7) Test Reporting


* This 7 phases of STLC work together to make sure systematic and structured approch to testing.
  Resulting in high-quality software that meets user expectations. 


1) Requirement Analysis: 
------------------------
    1. Understand the requirements: Read the documents with the team to know what the software 
       is supposed to do. 
    
    2. Identifiy what needs testing: Figure out which features or parts need to testbed. 

    3. Ask Questions: if anything is unclear, ask stakeholders (developers/BAs, Client) to avoid confusion later.

    4. Define testing objects: Decide what the goal of testing (make sure login works, check form validaitons, icons, links)

    5. Prepare High Level Notes: Make a rough list of all ares that need attendion during testing.
  
    Example: 
    >>>>>>>>
    i) for suppose your testing an online flipkart application. 
    ii) in this phase, you understand that users sould be able to login 
        in the browser, and can add it into cart, place orders. 
    iii) you talk to the product owener to confirm if 'guest checkout' is allowed or not.

    
2) Test Planning: 
-----------------
    1) write te testplan: document your approch to testing: what/how/and when you will test. 
    
    2) Setup the scope: Clarify what features are in scope (login/add cart/roderplacing/book order) and 
       out of scope (admin panel)
    
    3) Assign roles: decide who will test which features. 

    4) Create a Schedule: plan dates for test case writing/execution/and completion.

    5) Identify risks: think ahead: what if the pyament API is down? or 
       what if the test evironment crashes 
    
    6) Ensure coverage: make sure all important features have testcases. 

    Example:
    >>>>>>>>
    i) you plan to test in Chrome and Firefox (only defined scope)
    ii) you assign Login testing to testing A and Payment testing to Tester B. 
    iii) you decide testing will start on Mondy and Finish by Friday. 
    iv) you note a risk: the payment gateway is still under development, so testing may be 
        delayed. 
    v) you make sure the main flows: login/serach products/add to cart/checkout are all covered.

3) Test Design: 
---------------
    1) Write testcases or test scenarios: write step-by-step instructions to check each feature
    
    2) Define testdata: prepare inputs needed for testing (username/password/payment information)

    3) Review testcase: Go through the test cases to make sure they are correct and complete.

    4) Organize tests by priority: mark which testcase are critical (like login) and which are less urgent.

    Examples:
    >>>>>>>>>
    i) Login with valid and invalid credentials
    ii) Add product items to the cart and check if total price updates.
    iii) Apply coupon code and see if the discount is applied. 
    iv) 

    
 4) Test Environment Setup:
 --------------------------
    1) Prepare the test environment: Set up required hardware/software, servers, and network.
   
    2) Install test build: Deploy the application version to be tested.
    
    3) Configure required tools: Logging tools, automation tools, test management tools.

    Verify Environment Readiness: Run a smoke test to ensure the environment is stable.

    Example:
    >>>>>>>>
    Set up the staging server with the latest version of the app.
    Install test browsers like Chrome/Firefox with correct versions.
    Check if APIs are accessible and database is correctly loaded.

  
4) Test Execution: 
------------------
    1) Run the testcases: start testing each case step-by-step.
    
    2) Mark results: mark each test as 'pass' or 'fail' on whether the expected 
                     results matches the actual result. 
    
    3) Log defects for failed tests: if somthing doesn't work, record it as a bug 
                                     (with details and screenshots if needed.)
    
    Examples:
    >>>>>>>>>
    i) Your run your testcase: add item to cart and check price update 
    ii) the test fails because the cart dosen't update the total 
    iii) you log this bug: cart total not updating when new item is added. 

5) Defect tracking: (Find and Fix bugs):
----------------------------------------
    1) Report the bugs to developers: share the issues with the dev team 
       through bug tracking tools (like jira/bugzilla)
    
    2) work together to fix the issues: Developers fix the bugs and share the 
       update version for retesting. 
    
    3) Re-test the fixed bugs: Run the failed test cases again to make sure
       the issue is resolved.
    
    Examples:
    >>>>>>>>>
    i) the developers fixes the 'cart total not updating' bug. 
    ii) you test it again and now it works -- the total updates correctly.
    iii) you mark the bug as resolved or closed. 

6) Test Reporting(Reporting and Analysis):
------------------------------------------
    1) Prepare a test summary report: summarize how many testcases passed/failed 
       and were skipped.
    
    2) Analyze the results: see how many stable the product is, and if any risky 
       ares remain. 
    
    3) share feedback with Stackholders: Send reports and disscuss the testing 
       outcome with the team or managers.
    
    Examples:
    >>>>>>>>>
    i) you tested 50 scenarios: 45 passed/ 3 failed/ 2 skipped (due to missing features)
    ii) you prepare a summary and share it in the final test review meeting, 
        suggesting the app is mostrly ready but need minar fixes before release.

"""