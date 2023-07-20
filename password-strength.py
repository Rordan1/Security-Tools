
import re

## Complexity: It should include a combination of uppercase and lowercase letters, numbers, and special characters (e.g., @, #, $, %). T

##. Unpredictability: Avoid using predictable patterns or common substitutions (e.g., "P@ssw0rd" or "12345678"). 

##. Unique: It should be unique and not used for multiple accounts.

##. No personal information: Avoid using personal information such as your name, birthdate, or address. 

##. Randomness: Generate passwords randomly rather than using easily guessable words or phrases. 

##. Regularly updated: Change your password periodically, especially for sensitive accounts. 

## Regularly updating your password reduces the risk of long-term compromise.

## Two-factor authentication (2FA): Whenever possible, enable two-factor authentication. 

##### Length: Password should be at least 12 characters long or longer.

def check_password_length(password):

    bad = "Your password does not meet the minimum length qualifications"

    mid = "Your password has a moderate length"

    good = "Your password is a strong length password"

    if len(password) <= 6:
        return bad
    elif len(password) >= 7 and len(password) <= 12:
        return mid
    else:
        return good
    
### Valid input that will can not be used for a hacking techniques such as SQLi injection or XSS ###
    
def input_validation(password):

    dangerous_characters =  r'[\/ \\ \& \' \!]'

    for char in password:
        if char in dangerous_characters:
            return True
    else:
        return False

def main():

    User1_test = input("enter a password: ")
    result = check_password_length(User1_test)
    result2 = input_validation(User1_test)
    print(result)

    if result2 == True:
        print("Your password is flagged as potentially malicious code, please remove any of these characters /, \, &, or ' ")
    elif result2 == False:
        print("Also, your password has passed the input validation check")
        

if __name__ == "__main__":
    main()