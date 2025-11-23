import json
from dataclasses import dataclass

@dataclass
class Student:
    """
    Represents a single student record in the system.
    Using dataclasses simplifies creating objects and provides helpful defaults.
    """
    student_id: str
    name: str
    age: int
    grade: str
    major: str

    def to_dict(self):
        """Converts the Student object into a dictionary for easy saving (serialization)."""
        return {
            'student_id': self.student_id,
            'name': self.name,
            'age': self.age,
            'grade': self.grade,
            'major': self.major
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Student object from a dictionary (deserialization)."""
        return cls(
            student_id=data.get('student_id'),
            name=data.get('name'),
            age=data.get('age'),
            grade=data.get('grade'),
            major=data.get('major')
        )

    def __str__(self):
        """Defines the friendly string representation of a student."""
        return (f"ID: {self.student_id:<5} | Name: {self.name:<20} | Age: {self.age:<3} "
                f"| Grade: {self.grade:<5} | Major: {self.major}")

# Example of how you could use the class (optional)
if __name__ == '__main__':
    s = Student(student_id="S101", name="Alice Johnson", age=19, grade="Sophomore", major="Computer Science")
    print(s)
    print(s.to_dict())