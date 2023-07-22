
import re

##### Length: Password should be at least 12 characters long or longer.

def check_password_length(password):

    bad = "Your password does not meet the minimum length qualifications."

    mid = "Your password is a moderate length."

    good = "Your password is a strong length."

    if len(password) <= 6:
        return bad
    elif len(password) >= 7 and len(password) <= 12:
        return mid
    else:
        return good
    
### Valid input that will can not be used for a hacking techniques such as SQLi injection, directory traversal, or XSS ###
    
def input_validation(password):

    # sql_injection_indicator
    # directory_traversal_indicator
    # xss_indicator
    # shell_code_execution
    # encoding

    malicious_strings = ["1=1", '1=1', "../", "..\\", "<script>", "!#", "SELECT", "FROM", "WHERE", "select", "from", "where", "%0", "%1", "%2", "%3", "%4", "%5", "%6", "%7", "%8", "%9"]

    for malicious_string in malicious_strings:
        if malicious_string in password:
            return True
        
    return False
   
    

## Complexity: It should include a combination of uppercase and lowercase letters, numbers, and special characters (e.g., @, , $, ). 

def input_complexity(password):
     
   special_characters = ["@", "$", "'", "/", "!", "#",	"%", "&", "(", ")", "*", "+", "-",".", "/", ":" ,";", "<", "=", ">", "?"]

   for char in special_characters:
        if char in password:
            return True
   return False


##. Unpredictability: Avoid using predictable patterns or common substitutions (e.g., "P@ssw0rd" or "12345678"). 


def main():

    User1_test = input("enter a password: ")
    result = check_password_length(User1_test)
    result2 = input_validation(User1_test)
    result3 = input_complexity(User1_test)
    print(result)

    if result3 == True:
        print("Additionally, your password meets the minimum complexity standards.")
    if result3 == False:
        print("And unfortunately, your password does not meet the minimum complexity standards. Please add a special character.")

    if result2 == True:
        print("And unfortunately your password was flagged as potentially malicious code. Please try a different password")
    elif result2 == False:
        print("Lastly, your password has successfully passed the input validation check.")
        
    

if __name__ == "__main__":
    main()