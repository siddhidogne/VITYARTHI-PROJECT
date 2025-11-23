from sms_controller import StudentManagementSystem
import sys

# Instantiate the controller, which automatically loads data
sms = StudentManagementSystem()

def display_menu():
    """Prints the main menu options to the console."""
    print("\n=============================================")
    print("      STUDENT MANAGEMENT SYSTEM (v1.0)       ")
    print("=============================================")
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Find Student by ID")
    print("4. Update Student Information")
    print("5. Delete Student Record")
    print("6. Exit System")
    print("=============================================")

def handle_add_student():
    """Handles the user interaction for adding a new student."""
    print("\n--- ADD NEW STUDENT ---")
    student_id = input("Enter Student ID (e.g., S101): ").strip().upper()
    name = input("Enter Student Name: ").strip()
    age_str = input("Enter Age: ").strip()
    grade = input("Enter Grade Level (e.g., Freshman, Senior): ").strip()
    major = input("Enter Major: ").strip()
    
    success, message = sms.add_student(student_id, name, age_str, grade, major)
    print(f"\n[RESULT] {message}")

def handle_view_student():
    """Handles the user interaction for viewing a single student."""
    print("\n--- FIND STUDENT ---")
    student_id = input("Enter Student ID to find: ").strip().upper()
    
    success, result = sms.view_student(student_id)
    if success:
        print("\n[RESULT] Student Found:")
        print(f"  {result}")
    else:
        print(f"\n[RESULT] {result}")

def handle_update_student():
    """Handles the user interaction for updating student details."""
    print("\n--- UPDATE STUDENT ---")
    student_id = input("Enter Student ID to update: ").strip().upper()

    # First, check if the student exists
    success, student = sms.view_student(student_id)
    if not success:
        print(f"\n[RESULT] {student}")
        return

    print(f"\nUpdating: {student}")
    print("Enter new values (leave blank to keep current value):")
    
    new_data = {}
    
    new_name = input(f"New Name ({student.name}): ").strip()
    if new_name:
        new_data['name'] = new_name
        
    new_age = input(f"New Age ({student.age}): ").strip()