from peopleNclass import Student, Teacher, Class, Enrollment
from school import School


'''
The codes below is just a sample implementation of the student management system.
You are free to modify and use it to try out the code
'''

# Sample list of Student instances:
student1 = Student("John Doe", "1234")
student2 = Student("Jane Smith", "5678")
student3 = Student("Adam Johnson", "9101")
student4 = Student("Samantha Kim", "1121")
student5 = Student("Michael Lee", "3141")
student6 = Student("Oliver Chen", "5161")
student7 = Student("Isabella Wong", "7181")
student8 = Student("William Lee", "9202")
student9 = Student("Emily Lee", "1222")
student10 = Student("Daniel Kim", "2424")
student11 = Student("Sophia Park", "3642")
student12 = Student("Emma Lee", "4865")
student13 = Student("Ethan Smith", "6489")
student14 = Student("Grace Kim", "7821")
student15 = Student("Ava Jones", "9062")
student16 = Student("Jacob Lee", "1151")
student17 = Student("Mia Johnson", "1357")
student18 = Student("Joshua Lee", "1598")
student19 = Student("Chloe Park", "1882")
student20 = Student("Noah Kim", "2010")

# Sample list of Teacher instances:
teacher1 = Teacher("Mr. Johnson", "T1234")
teacher2 = Teacher("Ms. Smith", "T5678")
teacher3 = Teacher("Mr. Lee", "T9101")
teacher4 = Teacher("Ms. Kim", "T1121")
teacher5 = Teacher("Mr. Chen", "T3141")
teacher6 = Teacher("Ms. Wong", "T5161")
teacher7 = Teacher("Mr. Park", "T7181")
teacher8 = Teacher("Ms. Brown", "T9202")
teacher9 = Teacher("Mr. Davis", "T1222")
teacher10 = Teacher("Ms. Garcia", "T2424")
teacher11 = Teacher("Mr. Hernandez", "T3642")
teacher12 = Teacher("Ms. Jackson", "T4865")
teacher13 = Teacher("Mr. Lopez", "T6489")
teacher14 = Teacher("Ms. Martinez", "T7821")

# Sample list of Class instance:
class1 = Class("Mathematics", "MATH101")
class2 = Class("Science", "SCI101")
class3 = Class("English", "ENG101")
class4 = Class("History", "HIS101")
class5 = Class("Geography", "GEO101")
class6 = Class("Art", "ART101")
class7 = Class("Music", "MUS101")
class8 = Class("Physical Education", "PED101")
class9 = Class("Computer Science", "CSC101")
class10 = Class("Foreign Language", "FOR101")
class11 = Class("Economics", "ECO101")
class12 = Class("Biology", "BIO101")
class13 = Class("Chemistry", "CHE101")
class14 = Class("Physics", "PHY101")
class15 = Class("Political Science", "POL101")

'''
___________________________________________________________________
                                                                    '''


teacher_list = [teacher1, teacher2, teacher3, teacher4, teacher5]
student_list = [student1, student2, student3, student4, student5]
class_list = [class1, class2, class3, class4, class5]

school1 = School()

for t in teacher_list:
    school1.add_teacher(t)

print(school1.teachers)

for s in student_list:
    school1.add_student(s)

print(school1.students)

for c in class_list:
    school1.add_class(c)
print(school1.classes)

for c in class_list:
    for s in student_list:
        school1.enroll_student(s, c)

student1_remove_class = school1.remove_student(student1, class2)
print(student1.enrollments)
print(class2.enrollments)

grade_list = [85, 97, 95, 93, 89, 78]

enrollment = Enrollment(student1, class1)

for g in grade_list:
    school1.assign_grade(enrollment, g)

print(enrollment.grades)

class2_Students = school1.list_students_in_class(class2)
print(class2_Students)

student1_classes = school1.list_classes_for_student(student1)
print(student1_classes)

average_grade = school1.average_grade(enrollment)
print(average_grade)
