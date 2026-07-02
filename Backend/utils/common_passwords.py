from pathlib import Path

def is_common_password(password: str):

    file_path = Path(__file__).parent.parent / "data" / "common_passwords.txt"

    with open(file_path, "r") as file:
        common_passwords = {line.strip().lower() for line in file}

    return password.lower() in common_passwords
