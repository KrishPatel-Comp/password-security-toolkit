def detect_repeated_characters(password: str):

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False

def detect_sequential_patterns(password: str):

    password = password.lower()

    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789"
    ]

    for sequence in sequences:
        for i in range(len(sequence) - 2):
            part = sequence[i:i+3]

            if part in password:
                return True

            if part[::-1] in password:
                return True

    return False
def detect_keyboard_pattern(password: str):

    password = password.lower()

    patterns = [
        "qwertyuiop",
        "asdfghjkl",
        "zxcvbnm",
        "1234567890",
        "qazwsx",
        "1q2w3e4r"
    ]

    for pattern in patterns:
        for i in range(len(pattern) - 2):
            part = pattern[i:i+3]

            if part in password:
                return True

            if part[::-1] in password:
                return True

    return False