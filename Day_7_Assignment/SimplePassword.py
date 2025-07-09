import re

def check_password(password):
    errors = []
    # Length check
    if len(password) < 8:
        errors.append("Password must be minimum 8 characters long.")
    # Uppercase check
    if not any(c.isupper() for c in password):
        errors.append("Password must contain at least one uppercase letter.")
    # Should not start with a number
    if password and password[0].isdigit():
        errors.append("Password should not start with a number.")
    # Special character check
    if not any(c in '@#$' for c in password):
        errors.append("Password must contain at least one special character (@, #, $).")
    
    return errors

if __name__ == "__main__":
    pwd = input("Enter password: ")
    result = check_password(pwd)
    if not result:
        print("Password is valid.")
    else:
        print("Password is invalid:")
        for err in result:
            print("-", err)
