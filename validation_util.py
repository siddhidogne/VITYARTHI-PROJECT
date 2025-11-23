import re

def validate_student_id(student_id):
    """
    Validates if the student ID follows a simple 'SXXX' pattern (e.g., S101).
    """
    if not student_id:
        return False, "Student ID cannot be empty."
    if not re.match(r'^S\d{3}$', student_id):
        return False, "ID must be in the format 'S###' (e.g., S101)."
    return True, ""

def validate_age(age_str):
    """
    Validates if the age is a valid integer within a reasonable range (16-99).
    """
    try:
        age = int(age_str)
        if 16 <= age <= 99:
            return True, age
        else:
            return False, "Age must be between 16 and 99."
    except ValueError:
        return False, "Age must be a whole number."

def validate_name(name):
    """
    Validates if the name is not empty and only contains letters and spaces.
    """
    if not name or name.strip() == "":
        return False, "Name cannot be empty."
    if not re.match(r'^[a-zA-Z\s]+$', name):
        return False, "Name can only contain letters and spaces."
    return True, ""