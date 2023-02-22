class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.enrollments = []  # a list representing all the classes the student is enrolled in. created using the Enrollment object

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.student_id}")'


class Teacher:
    def __init__(self, name: str, teacher_id: str):
        self.name = name
        self.teacher_id = teacher_id
        self.classes = []  # a list containing all the classes the teacher is teaching. The items are Class objects.

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.teacher_id}")'


class Class:
    def __init__(self, name: str, class_id: str):
        self.name = name
        self.class_id = class_id
        self.teachers = []  # a list representing all the teachers teaching the class. the items are Teacher objects.
        self.enrollments = []  # a list representing all the students enrolled in the class. created using the Enrollment object

    def __repr__(self):
        return f'{self.__class__.__name__}("{self.name}", "{self.class_id}")'


class Enrollment:
    # student is a parameter representing an instance of the class Student
    # class_ is a parameter representing an instance of the class Class

    def __init__(self, student, class_):
        self.student = student
        self.class_ = class_
        self.grades = []  # a list of integers representing the grades the student has received in the class


class Assignment:
    def __init__(self, teacher, class_):
        self.teacher = teacher
        self.class_ = class_
