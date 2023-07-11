## Length: It should be at least 12 characters long or longer.

## Complexity: It should include a combination of uppercase and lowercase letters, numbers, and special characters (e.g., @, #, $, %). T

##. Unpredictability: Avoid using predictable patterns or common substitutions (e.g., "P@ssw0rd" or "12345678"). 

##. Unique: It should be unique and not used for multiple accounts.

##. No personal information: Avoid using personal information such as your name, birthdate, or address. 

##. Randomness: Generate passwords randomly rather than using easily guessable words or phrases. 

##. Regularly updated: Change your password periodically, especially for sensitive accounts. 

## Regularly updating your password reduces the risk of long-term compromise.

## Two-factor authentication (2FA): Whenever possible, enable two-factor authentication. 

list = input("enter a password: ")

not_good = "Your password does not meet the minimum qualifications"

good = "This is a strong password"

if len(list) <= 12:
    print(not_good)

elif len(list) > 12:
    print(good)

