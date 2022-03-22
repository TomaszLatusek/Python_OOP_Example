from Student import *
from Teacher import *
from Course import *

allStudents = [Student("Karol", "Zajac", "1234@student.edu.pl", "qwerty", "1234"), Student("Jakub", "Krulik", "1235@student.edu.pl", "qwerty", "1235"),
               Student("Wojciech", "Wrona", "1236@student.edu.pl", "qwerty", "1236"), Student("Tomasz", "Wilk", "1237@student.edu.pl", "qwerty", "1237")]

allTeachers = [Teacher("Marek", "Dudek", "marek.dudek@edu.pl", "qwerty"), Teacher("Justyna", "Lupa",
                                                                                  "justyna.lupa@edu.pl", "qwerty"), Teacher("Dawid", "Mor", "dawid.mor@edu.pl", "qwerty")]

allUsers = allStudents + allTeachers

allCourses = [Course("Maths", "M1", allTeachers[0]), Course("Algebra", "A1", allTeachers[0]), Course(
    "Biology", "B1", allTeachers[1]), Course("Physics", "P1", allTeachers[2])]


for student in allStudents:
    for course in allCourses:
        student.addToCourse(course)
        course.addStudent(student)

for teacher in allTeachers:
    for course in allCourses:
        if(teacher == course.teacher):
            teacher.addCourse(course)