import math

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

def analyze_password(password: str):

    length = len(password)
    entropy = calculate_entropy(password)
    crack_time = estimate_crack_time(entropy)
    has_repeated = detect_repeated_characters(password)
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
        "strength": strength,
        "length": length,
        "has_uppercase": has_uppercase,
        "has_lowercase": has_lowercase,
        "has_number": has_number,
        "has_special": has_special,
        "suggestions": suggestions
    }