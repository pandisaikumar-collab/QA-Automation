"""
Bug Life Cycle: 
===============
1) The life cycle is the process a bug (defect/issue) goes through from the 
   moment it is found unitl it is resolved and closed. 

2) It helps to teams track/manage/and fix bugs efficiently to ensure software quality.


Common Stages of Bug Life Cycle:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

1) New
2) Assigned 
3) Opend 
4) In-progress (or fixed)
5) Retest 
6) Varified 
7) Closed 
8) Reopended (optional)
9) Rejected / Duplicate/ Not a bug (Optional)


1) New:
-------
    1. The tester finds a bug and logs it in a bug tracking tool 
    2. The bug is now in the 'New' state and waiting for review 

    Example:
    >>>>>>>>
    i) you find that the "apply coupon" button desen't work 
    ii) you raise a bug in jira and mark it New. 

2) Assigned: 
------------
    1. The bug is reviewd by the Test Lead or Project Manager, who assigns 
       it to a developer 
    
    Example:
    >>>>>>>>
    i) your lead assigns the coupon bug to developer X.
    ii) status changes from New-> Assigned. 

3) Opend: 
---------
    1. The assigned developer reviews the bug start working on fixing it. 

    Example: 
    >>>>>>>>
    i) X is starts looking into why the coupon button fails and confirms it's real issue
    ,status changes to open 

4) In-progress: 
---------------
    1. The developer fixes the bug and updates the bug status as fixed (or in-progress while working)
    2. The code is sent for testing again (may go thorugh code review or deployment too).

    Example: 
    >>>>>>>>
    i) X fixes the bug and updates Jira,
    ii) Status --> Fixed 

5) Retest: 
----------
    1. The tester now re-test the same scenario to confirm the bug is realy fixed. 

    Example: 
    >>>>>>>>
    i) you test the 'apply coupon' button again 
    ii) now it shows the correct discount 

6) Verified: 
------------
    1. if the bug no longer appears during re-testing, the tester marks it as verifed. 
    
    Example: 
    >>>>>>>>
    i) you mark the coupon bug as Verifed since it works correctly now. 

7) Closed: 
----------
    1. Once the fix is verfied and approved, the bug is marked as closed
    2. this means the bug is resolved and no further action is needed. 

    Example: 
    >>>>>>>>
    i) after final confirmtaion, the bug is marked as closed. 

8) Re-opened: 
-------------
    1. If the bug still exists after being marked as fixed, the tester Re-opens it.
    
    Examples:
    >>>>>>>>>
    i) if the coupon button still desnt' apply the discount properly. 
    ii) you re-open the bug and add a comment 'Issue not resolved'

9) Rejected/Duplicate/Not a Bug (optional):
-------------------------------------------
    1. sometimes bugs may be closed without fix. 
    2. Rejected: the bug is not valid or cannot be repreoduced 
    3. Duplicate: The same bug is already reported. 
    4. Not a Bug: The behavior is intentional or as per requirment.

    Example: 
    >>>>>>>>
    i) you report a bug about missing field, but the product team says it was 
       removed on purpose --> status: not a bug 
    ii) you report an error message bug, but it's already reported by another tester 
        status: Duplicate

"""