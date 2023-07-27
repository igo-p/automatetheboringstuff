import re

def is_strong_pwd(pwd_str):
    pwd_detection = re.compile(r'''
                        (?=.*[a-z])     # Positive lookahead to see if there's at least 1 lowercase letter
                        (?=.*[A-Z])     # Positive lookahead to see if there's at least 1 uppercase letter
                        (?=.*\d)        # Positive lookahead to see if there's at least 1 digit
                        (?=.*.{8,})     # Positive lookahead to see if the password is at least 8 characters long
    ''',re.VERBOSE)

    return re.match(pwd_detection,pwd_str) != None

print(is_strong_pwd('1wDonwkd'))
                           
