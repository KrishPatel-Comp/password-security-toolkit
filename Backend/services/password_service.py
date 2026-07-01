import math
from pathlib import Path

def calculate_entropy(password: str):

    charset = 0

    if any(c.islower() for c in password):
        charset += 26

    if any(c.isupper() for c in password):
        charset += 26

    if any(c.isdigit() for c in password):
        charset += 10

    if any(not c.isalnum() for c in password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)

    return round(entropy, 2)
def estimate_crack_time(entropy):

    if entropy < 28:
        return "Instantly"

    elif entropy < 36:
        return "A few minutes"

    elif entropy < 60:
        return "Several hours"

    elif entropy < 80:
        return "Several years"

    else:
        return "Centuries"   
    
def detect_repeated_characters(password: str):

    for i in range(len(password) - 2):
        if password[i] == password[i + 1] == password[i + 2]:
            return True

    return False

def is_common_password(password: str):

    file_path = Path(__file__).parent.parent / "data" / "common_passwords.txt"

    with open(file_path, "r") as file:
        common_passwords = {line.strip().lower() for line in file}

    return password.lower() in common_passwords

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

def analyze_password(password: str):

    length = len(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)
    has_repeated = detect_repeated_characters(password)
    is_common = is_common_password(password)
    has_sequence = detect_sequential_patterns(password)
    has_keyboard_pattern = detect_keyboard_pattern(password)
    has_uppercase = any(c.isupper() for c in password)
    has_lowercase = any(c.islower() for c in password)
    has_number = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = 0

    # Length Score
    if length >= 16:
        score += 35
    elif length >= 12:
        score += 30
    elif length >= 8:
        score += 20

    # Character Score
    if has_special:
        score += 20

    if has_number:
        score += 20

    if has_uppercase:
        score += 15

    if has_lowercase:
        score += 10

    # Suggestions
    suggestions = []

    if length < 8:
        suggestions.append("Use at least 8 characters.")

    if not has_uppercase:
        suggestions.append("Add at least one uppercase letter.")

    if not has_lowercase:
        suggestions.append("Add at least one lowercase letter.")

    if not has_number:
        suggestions.append("Add at least one number.")

    if not has_special:
        suggestions.append("Add at least one special character.")

    if length < 12:
        suggestions.append("Consider using 12 or more characters for better security.")
    
    if has_repeated:
        suggestions.append("Avoid repeating the same character multiple times.")

    if is_common:
        suggestions.append("This is a commonly used password. Choose something more unique.")

    if has_sequence:
        suggestions.append("Avoid sequential patterns like '123' or 'abc'.")
    
    if has_keyboard_pattern:
        suggestions.append("Avoid keyboard patterns like 'qwerty' or 'asdf'.")

    if is_common:
        score -= 30
        

    if has_sequence:
        score -= 15
       
    if has_keyboard_pattern:
        score -= 15

    score = max(score, 0)


    # Determine strength
    if score >= 90:
        strength = "Very Strong"
    elif score >= 70:
        strength = "Strong"
    elif score >= 50:
        strength = "Medium"
    elif score >= 25:
        strength = "Weak"
    else:
        strength = "Very Weak"

    return {
        "score": score,
        "entropy": entropy,
        "crack_time": crack_time,
        "has_repeated_characters": has_repeated,
        "is_common_password": is_common,
        "has_sequential_pattern": has_sequence,
        "has_keyboard_pattern": has_keyboard_pattern,
        "strength": strength,
        "length": length,
        "has_uppercase": has_uppercase,
        "has_lowercase": has_lowercase,
        "has_number": has_number,
        "has_special": has_special,
        "suggestions": suggestions
    }