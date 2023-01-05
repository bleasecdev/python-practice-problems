# Complete the check_password function that accepts a
# single parameter, the password to check.
#
# A password is valid if it meets all of these criteria
#   * It must have at least one lowercase letter (a-z)
#   * It must have at least one uppercase letter (A-Z)
#   * It must have at least one digit (0-9)
#   * It must have at least one special character $, !, or @
#   * It must have six or more characters in it
#   * It must have twelve or fewer characters in it
#
# The string object has some methods that you may want to use,
# like ".isalpha", ".isdigit", ".isupper", and ".islower"

def check_password(password):
    try_again = 'Your password does not meet the requirements please review and try again.'
    if len(password) > 12 or len(password) < 6:
        print(try_again)
        return False
    if not any(char.islower() for char in password):
        print(try_again)
        return False
    if not any(char.isupper() for char in password):
        print(try_again)
        return False
    if not any(char.isdigit() for char in password):
        print(try_again)
        return False
    if not any(char.isalpha() for char in password):
        print(try_again)
        return False
    if not any(char in '$!@' for char in password):
        print(try_again)
        return False
    print('Thank you for your password')
    return True
    

check_password('Sterling!0')




