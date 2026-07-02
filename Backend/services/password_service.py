from utils.entropy import calculate_entropy, estimate_crack_time
from utils.pattern_detection import detect_repeated_characters
from utils.pattern_detection import detect_sequential_patterns
from utils.pattern_detection import detect_keyboard_pattern
from utils.common_passwords import is_common_password  


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