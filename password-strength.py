
import re

##### Length: Password should be at least 12 characters long or longer.

def check_password_length(password):

    bad = "Your password does not meet the minimum length qualifications."

    mid = "Your password has a moderate length."

    good = "Your password is a strong length password."

    if len(password) <= 6:
        return bad
    elif len(password) >= 7 and len(password) <= 12:
        return mid
    else:
        return good
    
### Valid input that will can not be used for a hacking techniques such as SQLi injection, directory traversal, or XSS ###
    
def input_validation(password):

    # r"(\.\.\/ \.\.\.\\ \& \' \= \%'[0-9]' \? \+ )"
    # sql_injection_indicator
    # directory_traversal_indicator
    # xss_indicator
    # shell_code_execution

    malicious_strings = ["1=1", "../", "..\\", "<script>", "!#" ]

    for malicious_string in malicious_strings:
        if malicious_string in password:
            return True
        
    return False
   
    

## Complexity: It should include a combination of uppercase and lowercase letters, numbers, and special characters (e.g., @, , $, ). 

# def input_complexity(password):
     



##. Unpredictability: Avoid using predictable patterns or common substitutions (e.g., "P@ssw0rd" or "12345678"). 


def main():

    User1_test = input("enter a password: ")
    result = check_password_length(User1_test)
    result2 = input_validation(User1_test)
    print(result)

    if result2 == True:
        print("Your password is flagged as potentially malicious code, please try a different password")
    elif result2 == False:
        print("Also, your password has passed the input validation check.")
        

if __name__ == "__main__":
    main()