
import re

##### Password should be at least 12 characters long or longer.

def check_password_length(password):

    bad = "Your password does not meet the minimum length qualifications. Please try again."

    mid = "Your password is a moderate length."

    good = "Your password is a strong length."

    if len(password) <= 6:
        print(bad)
        quit()

    elif len(password) >= 7 and len(password) <= 12:
        return mid
    
    else:
        return good
    

### Valid input that can not be used for a hacking techniques
    
def input_validation(password):

    # sql_injection_indicator
    # directory_traversal_indicator
    # xss_indicator
    # shell_code_execution
    # encoding

    malicious_strings = ["1=1", '1=1', "../", "..\\", "<script>", "#!", "SELECT", "FROM", "WHERE", "select", "from", "where", "%0", "%1", "%2", "%3", "%4", "%5", "%6", "%7", "%8", "%9"]

    for malicious_string in malicious_strings:
        if malicious_string in password:
            return True
        
    return False
    

## Include a combination of uppercase and lowercase letters, numbers, and special characters. 

def input_complexity(password):
     
   special_characters = ["@", "$", "'", "/", "!", "#",	"%", "&", "(", ")", "*", "+", "-",".", "/", ":" ,";", "<", "=", ">", "?", "^"]

   for char in special_characters:
        if char in password:
            return True
   return False

## Make sure that there are not multiple repetitive numbers.

def repeating_numbers(password): 
    repeating_digits = 0 
    consecutive_digits = 0 
    
    for char in password: 
        if char.isdigit(): 
            repeating_digits += 1 
            consecutive_digits = 0 
            
            if repeating_digits >= 3 or repeating_digits >= 3:
                return True
            
        else: 
            repeating_digits = 0
            consecutive_digits = 0
            
    return False

## Make sure that there are not multiple repetitive letters

def repeating_characters(password):
    repeating_chars = 0
    consecutive_chars = 0

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            repeating_chars += 1
            consecutive_chars += 1

            if repeating_chars >= 3 or consecutive_chars >= 3:
                return True
        else:
            repeating_chars = 0
            consecutive_chars += 1

    return False


## Merge all checks and give an output message

def main():

    User1_test = input("enter a password: ")
    result = check_password_length(User1_test)
    
    print(result)

    result3 = input_complexity(User1_test)
    result2 = input_validation(User1_test)
    results4 = repeating_numbers(User1_test)
    results5 = repeating_characters(User1_test)
   
    
   
    if result3 == True:
        print("Additionally, your password meets the .")
    else:
        print("But unfortunately, your password does not meet the minimum complexity standards. Please add a special character.")
        quit()
 
    if results4 == True:
        print("Your password has multiple consecutive numbers. Please try a different password.")
        quit()
    elif results4 == False:
        print("Your password has passed the consecutive numbers check.")

    if results5:
        print("Your password has multiple consecutive characters. Please try a different password.")
        quit()
    else:
        print("Your password has passed the consecutive characters check.")

    if result2 == True:
        print("But unfortunately your password was flagged as potentially malicious code. Please try a different password.")
        quit()
    elif result2 == False:
        print("And lastly, your password has successfully passed the input validation check. \n This means it meets complexity standards")

   

if __name__ == "__main__":
    main()