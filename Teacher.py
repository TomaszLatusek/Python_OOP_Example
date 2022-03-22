from User import *


class Teacher(User):

    def __init__(self, name, lastName, email, password):
        User.__init__(self, name, lastName, email, password)
        self.courses = []

    def addCourse(self, course):
        self.courses.append(course)

    def findCourseById(self, courseID):
        for x in self.courses:
            if x.id == courseID:
                return x
        print("Couldn't find a course with the ID of {0}".format(courseID))

    def showCourses(self):
        i = 1
        for course in self.courses:
            print("%d. %s %s" % (i, course.id, course.name))
            i += 1

    def menu(self):
        self.chooseCourse()

    def chooseCourse(self):
        x = 1
        while(x != 0):
            print("\nChoose the course: ")
            self.showCourses()
            x = input("Your option: ")
            if(x == 0):
                continue
            self.courseOptions(x)

    def courseOptions(self, course):
        x = 1
        while(x != 0):
            print("1. List of students")
            print("2. Course raport")
            x = input("Your option: ")
            if(x == 1):
                self.chooseStudent(course)
            if(x == 2):
                self.courseRaport(course)


    def courseRaport(self, theCourse):
        studentsWithNoFinalGrade = 0
        studentsAboutToFail = 0
        averageOfTheGroup = 0

        course = self.courses[theCourse - 1]
        numberOfStudents = len(course.students)

        for student in course.students:
            if(student.hasFinalGrade(course) == False):
                studentsWithNoFinalGrade += 1
            if(student.getAverage(course) <= 2.0):
                studentsAboutToFail += 1
            averageOfTheGroup += student.getAverage(course)

        averageOfTheGroup /= numberOfStudents

        print("Number of students in the group: %d" %numberOfStudents)
        print("Number of students with average <=2.0: %d" %studentsAboutToFail)
        print("Number of students with no final grade: %d" %studentsWithNoFinalGrade)
        print("Average of the group: %f" %averageOfTheGroup)


    def chooseStudent(self, course):
        x = course
        while(x != 0):
            print("\nChoose the student: ")
            self.courses[course - 1].showListOfStudents()
            x = input("Your option: ")
            if(x == 0):
                continue
            self.chooseAction(course, x)

    def chooseAction(self, course, student):
        x = student
        theCourse = self.courses[course - 1]

        while(x != 0):
            print("\nChoose the action: ")
            print("1. Add grade")
            print("2. Remove grade")
            print("3. Show grades")
            print("----------------")
            print("4. Add final grade")
            print("5. Modify final grade")
            print("6. Show final grade")
            x = input("Your option: ")
            if(x == 0):
                continue
            if(x == 1):
                self.courses[course - 1].students[student -
                                                  1].addGrade(theCourse)
            if(x == 2):
                self.courses[course - 1].students[student -
                                                  1].removeGrade(theCourse)
            if(x == 3):
                self.courses[course - 1].students[student -
                                                  1].showGradesFromTheCourse(theCourse)
            if(x == 4):
                self.courses[course - 1].students[student -
                                                  1].addFinalGrade(theCourse)
            if(x == 5):
                self.courses[course - 1].students[student -
                                                  1].modifyFinalGrade(theCourse)
            if(x == 6):
                self.courses[course - 1].students[student -
                                                  1].showFinalGrade(theCourse)