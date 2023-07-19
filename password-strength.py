##### Length: It should be at least 12 characters long or longer.

## Complexity: It should include a combination of uppercase and lowercase letters, numbers, and special characters (e.g., @, #, $, %). T

##. Unpredictability: Avoid using predictable patterns or common substitutions (e.g., "P@ssw0rd" or "12345678"). 

##. Unique: It should be unique and not used for multiple accounts.

##. No personal information: Avoid using personal information such as your name, birthdate, or address. 

##. Randomness: Generate passwords randomly rather than using easily guessable words or phrases. 

##. Regularly updated: Change your password periodically, especially for sensitive accounts. 

## Regularly updating your password reduces the risk of long-term compromise.

## Two-factor authentication (2FA): Whenever possible, enable two-factor authentication. 

def check_password_strength(password):

    bad = "Your password does not meet the minimum qualifications"

    mid = "Your password has a moderate level complexity"

    good = "Your password is a strong password"

    if len(password) <= 8:
        return bad
    elif len(password) >= 9 and len(password) <= 12:
        return mid
    else:
        return good

User1_test = input("enter a password: ")
result = check_password_strength(User1_test)
print(result)

