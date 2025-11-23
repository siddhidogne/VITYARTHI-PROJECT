from student_model import Student
from data_manager import load_data, save_data
from validation_util import validate_student_id, validate_age, validate_name

class StudentManagementSystem:
    """
    The core controller class that manages the student records.
    It handles CRUD operations and data persistence.
    """
    def __init__(self):
        # Load existing data upon system initialization
        self.students = load_data()
        print(f"System initialized. Loaded {len(self.students)} student records.")

    def _find_student_index(self, student_id):
        """Helper to find the list index of a student by ID."""
        return next((i for i, s in enumerate(self.students) if s.student_id == student_id), -1)

    def add_student(self, student_id, name, age_str, grade, major):
        """Adds a new student after thorough validation."""
        # 1. Validate ID format
        is_valid_id, id_msg = validate_student_id(student_id)
        if not is_valid_id:
            return False, f"Validation Failed: {id_msg}"

        # 2. Check for duplicate ID
        if self._find_student_index(student_id) != -1:
            return False, f"Error: Student with ID '{student_id}' already exists."

        # 3. Validate Age
        is_valid_age, age_result = validate_age(age_str)
        if not is_valid_age:
            return False, f"Validation Failed: {age_result}"
        age = age_result # Age is now guaranteed to be an integer

        # 4. Validate Name
        is_valid_name, name_msg = validate_name(name)
        if not is_valid_name:
            return False, f"Validation Failed: {name_msg}"

        # If all checks pass, create and add the student
        new_student = Student(
            student_id=student_id,
            name=name.strip(),
            age=age,
            grade=grade,
            major=major.strip()
        )
        self.students.append(new_student)
        self.save_changes()
        return True, f"Success! Student '{name.strip()}' ({student_id}) added."

    def view_student(self, student_id):
        """Retrieves and returns a single student record by ID."""
        index = self._find_student_index(student_id)
        if index != -1:
            return True, self.students[index]
        return False, f"Error: Student with ID '{student_id}' not found."

    def view_all_students(self):
        """Returns the entire list of student records."""
        if not self.students:
            return "No students registered in the system yet."
        
        # Sort by ID for clean display
        sorted_students = sorted(self.students, key=lambda s: s.student_id)
        
        output = ["--- CURRENT STUDENT ROSTER ---"]
        for s in sorted_students:
            output.append(str(s))
        output.append("------------------------------")
        return "\n".join(output)

    def update_student(self, student_id, new_data):
        """
        Updates fields of an existing student.
        new_data is a dictionary containing fields to update.
        """
        index = self._find_student_index(student_id)
        if index == -1:
            return False, f"Error: Cannot update. Student ID '{student_id}' not found."

        student_to_update = self.students[index]
        
        # Apply updates and validate where necessary
        if 'name' in new_data:
            is_valid_name, name_msg = validate_name(new_data['name'])
            if not is_valid_name:
                return False, f"Update Failed: {name_msg}"
            student_to_update.name = new_data['name'].strip()

        if 'age' in new_data:
            is_valid_age, age_result = validate_age(str(new_data['age']))
            if not is_valid_age:
                return False, f"Update Failed: {age_result}"
            student_to_update.age = age_result

        if 'grade' in new_data:
            student_to_update.grade = new_data['grade'].strip()

        if 'major' in new_data:
            student_to_update.major = new_data['major'].strip()
        
        self.save_changes()
        return True, f"Success! Student '{student_id}' updated."

    def delete_student(self, student_id):
        """Removes a student record by ID."""
        index = self._find_student_index(student_id)
        if index != -1:
            deleted_student_name = self.students[index].name
            del self.students[index]
            self.save_changes()
            return True, f"Success! Student '{deleted_student_name}' ({student_id}) has been removed."
        return False, f"Error: Cannot delete. Student ID '{student_id}' not found."

    def save_changes(self):
        """Calls the data persistence layer to save current state."""
        success = save_data(self.students)
        if success:
            print("[System Status: Data automatically saved to file.]")
        else:
            print("[System Status: Failed to save data! Check file permissions.]")