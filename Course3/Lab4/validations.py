import re

def validate_user(username, minlen):
    if minlen < 1:
        raise ValueError("minlen must be at least 1")

    # Usernames can't be shorter than minlen
    if len(username) < minlen:
        return False
    # Usernames can only use letters, numbers, dots, and underscores
    if not re.match('^[a-zA-Z][a-zA-Z0-9._]*$', username):
        return False
    return True

print(validate_user("blue.kale", 3))  # True
print(validate_user(".blue.kale", 3))  # False
print(validate_user("red_quinoa", 4))  # True
print(validate_user("_red_quinoa", 4))  # False
