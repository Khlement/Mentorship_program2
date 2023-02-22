from peopleNclass import Student, Teacher, Class, Enrollment, Assignment


class School:
    def __init__(self):
        self.students = []
        self.teachers = []
        self.classes = []

    def add_student(self, student):  # student is a parameter representing an instance of the class Student
        self.students.append(student)

    def add_teacher(self, teacher):  # teacher is a parameter representing an instance of the class Teacher
        self.teachers.append(teacher)

    def add_class(self, class_):  # class_ is a parameter representing an instance of the class Class
        self.classes.append(class_)

    def enroll_student(self, student, class_):
        enrollment = Enrollment(student, class_)
        student.enrollments.append(enrollment.class_)
        class_.enrollments.append(enrollment.student)

    def remove_student(self, student, class_):
        for pupil in class_.enrollments:
            if pupil == student:
                class_.enrollments.remove(pupil)
                student.enrollments.remove(class_)

    def assign_teacher(self, teacher, class_):
        assignment = Assignment(teacher, class_)
        teacher.classes.append(assignment.class_)
        class_.teachers.append(assignment.teacher)

    def assign_grade(self, enrollment, grade: float):  # enrollment is a variable representing an instance of the class enrollment
        enrollment.grades.append(grade)

    def list_students_in_class(self, class_):
        return class_.enrollments

    def list_classes_for_student(self, student):
        return student.enrollments

    def list_teachers_for_class(self, class_):
        return class_.teachers

    def average_grade(self, enrollment):  # enrollment is a variable representing an instance of the class Enrollment
        total_grade = 0
        no_courses = len(enrollment.grades)

        for grade in enrollment.grades:
            total_grade += grade

        average_grade = total_grade / no_courses
        return average_grade
