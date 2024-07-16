import hashlib
import re


def hash(content):
    hashed_content = hashlib.sha256(content.encode()).hexdigest()
    return hashed_content


def CheckPasswordFormat(password):
    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return bool(re.match(pattern, password))
