import re

EMAIL_PATTERN = r'^[A-Za-z][A-Za-z0-9._]*@[A-Za-z]+\.(com|org|edu|net|in)$'
PASSWORD_PATTERN = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!])[A-Za-z\d@#$%&!]{8,}$'
MOBILE_PATTERN = r'^[6-9]\d{9}$'


def validate_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


def validate_password(password):
    return re.fullmatch(PASSWORD_PATTERN, password) is not None


def validate_mobile(mobile):
    return re.fullmatch(MOBILE_PATTERN, mobile) is not None


def main():
    email = input("Enter Email: ").strip()
    password = input("Enter Password: ").strip()
    mobile = input("Enter Mobile Number: ").strip()

    print()

    if validate_email(email):
        print("Valid Email")
    else:
        print("Invalid Email")

    if validate_password(password):
        print("Strong Password")
    else:
        print("Weak Password")

    if validate_mobile(mobile):
        print("Valid Mobile Number")
    else:
        print("Invalid Mobile Number")


if __name__ == "__main__":
    main()