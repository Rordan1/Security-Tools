
import re

##### Password should be at least 12 characters long or longer.

def check_password_length(password):

    bad = "\nYour password does not meet the minimum length qualifications. Please try again."

    mid = "\nYour password is a moderate length."

    good = "\nYour password is a strong length."

    if len(password) <= 6:
        print(bad)
        quit()

    elif len(password) >= 7 and len(password) <= 12:
        return mid
    
    else:
        return good
    

### Valid input that can not be used for a hacking techniques
    
def input_validation(password):

    # sql_injection
    # directory_traversal
    # xss
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


## Make sure that there are not multiple repetitive numbers consecutively.

def has_repeating_characters(password): 
    repeating_chars = 0 

    for i in range(len(password) - 2): 
        if password[i] == password[i + 1] == password[i + 2]: 
            repeating_chars += 1 
        else: repeating_chars = 0 
        
        if repeating_chars >= 3: 
            return True 
            
    for char in password: 
        if char.isdigit(): 
            repeating_chars += 1 
            
        else: repeating_chars = 0 
        
        if repeating_chars >= 3: 
            return True 
    
    return False

def main():

    User1_test = input("enter a password: ")
    result = check_password_length(User1_test)
    
    print(result + "\n")

    result3 = input_complexity(User1_test)
    result2 = input_validation(User1_test)
    results4 = has_repeating_characters(User1_test)
    
   
    if result3 == True:
        print("Your password has a sufficient number of special characters.\n")
    else:
        print("But unfortunately, your password does not meet the minimum complexity standards. Please add a special character.")
        quit()
 
    if results4 == True:
        print("Your password has multiple consecutive numbers or letters. Please try a different password.")
        quit()
    elif results4 == False:
        print("Additionally, your password has passed the consecutive numbers check.\n")

    if result2 == True:
        print("But unfortunately your password was flagged as potentially malicious code. Please try a different password.")
        quit()
    elif result2 == False:
        print("And lastly, your password has successfully passed the input validation check. \nThis means it meets complexity standards.")

   
if __name__ == "__main__":
    main()