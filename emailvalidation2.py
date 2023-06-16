#Python Project-2 Email validation with python using RegEx Module 
#^[a-z] starting must be from a-z
# + concatenation of condition
# [\._]? _ . must be one 
# [a-z 0-9] can contain any from 0-9 a-z
# +[@]\w having @ w for searching
# +[.]\w{2,3}$ . should be at the position 2,3 from reverse($)
import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your E-mail:")

if re.search(email_condition,user_email):
    print("Your E-mail is perfect.")
else:
    print("Your E-mail is Improper. \nMake it Proper!")