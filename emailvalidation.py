#email validation with string Functions
email=input("Enter Your E-mail:")#closet condition of gmail is g@g.(in) ()bracket must be changing
k,j,d=0,0,0
if len(email)>=6:#checking the length which will be minimum will be 6 characters
    if email[0].isalpha():#First character in the email must be 1
        if ("@" in email) and (email.count==1):#email must contain @ and it must be one time only
            if (email[-4]==".") ^ (email[-3]):#taking negative index number for checking dot in the email, ^ xor operator due to true and false condition
                for i in email:# iteration of for loop for checking string at each position 
                    if i==i.isspace():#checks either there is space in the email 
                        k=1
                    elif i.isalpha():#check that the i is aplhabet or not
                        if i==i.upper():#converts i into the upper case letter 
                            j=1
                    elif i.isdigit():#checks that the i is digit or not 
                        continue #continues the for loop
                    elif i=="_" or i=="." or i=="@":
                        continue #continues the for loop
                    else:#if other characters used in email it shows invalid email 
                        d=1        
                if k==1 or j==1 or d==1:#for space in the email
                    print("Wrong E-mail: \nEmail Can't have space.")#5 for the fifth condition
                else:
                    print("Your Email is perfect.")
            else:
                print("Wrong E-mail: \nInvalid domain or the dot is mismatched.")#4 for the fourth condition
        else:
            print("Wrong E-mail: \nE-mail must have only one @ and must have sufficent domain name.")#3 for the third condition
    else:
        print("Wrong E-mail: \nFirst Character in E-mail must be Alphabet.")#2 for the second condition
else:
    print("Wrong E-mail: \nCheck the Length of your e-mail Must be min.6.")#1 for the first condition
