# This file will be use for customize value of the field in the database 

# List of current setup of designation of the company (ex. Service Advisor) and 
# other branch or department where hierachy of job title is a must included

# TODO: All this value will be manualy inputted from an UI form
DESIGNATION = (
    ("SVC", "SERVICE ADVISOR"),
    ("BRPSVC", "SERVICE ADVISOR FOR BRP"),
    ("ACCTMNGR", "ACCOUNTING MANAGER")
)


# Remarks for the status of the parts
REMARKS = (
    ("COMPLETE", "COMPLETED"),
    ("NOT COMPLETE", "NOT COMPLETE"),
    ("LACKING", "LACKING"),
)


# Parts number status and activity
# Company can customize this value 
# TODO: All this value be manually inputted by user using a form
PARTNUMBER_STATUS = (
    ("ACTIVE", "ACTIVE"),
    ("DEPRECATED", "DEPRECATED"),
    ("OBSOLETE", "OBSOLETE"),
    ("DEACTIVATED", "DEACTIVATED"),
)
