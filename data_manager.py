import json
from student_model import Student # Import the Student class

DATA_FILE = 'student_data.json'

def load_data():
    """
    Loads student data from the JSON file. If the file doesn't exist,
    it returns an empty list, allowing the application to start fresh.
    """
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            # Convert list of dictionaries back into list of Student objects
            return [Student.from_dict(d) for d in data]
    except FileNotFoundError:
        # This is a normal startup condition for a new system
        print(f"[{DATA_FILE}] not found. Starting with an empty database.")
        return []
    except json.JSONDecodeError:
        print(f"Error reading data from [{DATA_FILE}]. File might be corrupted.")
        return []

def save_data(students):
    """
    Saves the current list of Student objects to the JSON file.
    It serializes the objects into dictionaries first.
    """
    try:
        # Convert list of Student objects to a list of dictionaries for JSON
        data_to_save = [s.to_dict() for s in students]
        with open(DATA_FILE, 'w') as f:
            json.dump(data_to_save, f, indent=4)
        return True
    except IOError as e:
        print(f"Error saving data to [{DATA_FILE}]: {e}")
        return False