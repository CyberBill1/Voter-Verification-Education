#Program Written by Ede Ifeanyichukwu Barth
#About The Program:
#This Python program verifies if a prospective voter is eligible to vote by accepting input of year of birth from the user.
#Upon confirmation that one is eligible it directs the voter to proceed for Biometric Accreditation while educating the voter not to sell his/her vote.

M = input("What is your name?")
A = int (input("Please enter your year of Birth and press the Enter key"))
N = M
B = 2022
Age = (B - A)
if Age < 18 :
    print("You are not eligible to vote")
elif Age >= 70 :
    print("Sorry,you are too old to vote")
else:
    print("You are eligible to vote \n"+
          "Proceed for Accreditation")
    print(N,"DON'T SELL YOUR VOTE!!!")
