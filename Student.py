from calendar import c
from operator import truediv
from Grade import Grade
from User import *


class Student(User):

    def __init__(self, name, lastName, email, password, id):
        User.__init__(self, name, lastName, email, password)
        self.id = id
        self.courses = []
        self.grades = []
        self.finalGrades = []

    def toString(self):
        return '{0} {1} {2}'.format(self.id, self.name, self.lastName)

    def addToCourse(self, course):
        self.courses.append(course)

    def showCourses(self):
        for course in self.courses:
            print(course.id, course.name)

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
            self.showGradesFromTheCourse(self.courses[x - 1])

    def showGradesFromTheCourse(self, theCourse):
        if(len(self.grades) == 0):
            print("No grades")

        i = 1

        for grade in self.grades:
            if(grade.course == theCourse):
                print("%d. %s" % (i, grade.toString()))
                i += 1
        x = 1
        while(x != 0):
            print("\n1. Show average")
            print("2. Compare to others")
            x = input("Your option: ")
            if(x == 0):
                continue
            if(x == 1):
                print("%f" % self.getAverage(theCourse))
            if(x == 2):
                self.compareToOthers(theCourse)

    def getAverage(self, theCourse):
        i = 0
        sum = 0
        for grade in self.grades:
            if(grade.course == theCourse):
                sum += grade.value
                i += 1
        if(i == 0):
            return sum
        return sum / i

    def compareToOthers(self, theCourse):
        average = self.getAverage(theCourse)
        count = 0
        for student in theCourse.students:
            if(average < student.getAverage(theCourse)):
                count += 1
        print("%d people in your group have better average than you." % count)

    def addGrade(self, theCourse):
        print("You are adding grade to %s %s in the %s class" %
              (self.name, self.lastName, theCourse.name))
        value = input("Enter the value: ")
        comment = input("Enter the comment: ")
        self.grades.append(Grade(theCourse, value, comment, self))

    def removeGrade(self, theCourse):
        print("You are removing grade from %s %s in the %s class" %
              (self.name, self.lastName, theCourse.name))
        id = input("Choose which grade to remove: ")
        i = 1
        for grade in self.grades:
            if(grade.course == theCourse):
                if(i == id):
                    self.grades.remove(grade)
                i += 1

    def addFinalGrade(self, theCourse):
        print("You are adding final grade to %s %s in the %s class" %
              (self.name, self.lastName, theCourse.name))
        value = input("Enter the value: ")
        self.finalGrades.append(Grade(theCourse, value, "Final", self))

    def modifyFinalGrade(self, theCourse):
        print("You are modifying final grade from %s %s in the %s class" %
              (self.name, self.lastName, theCourse.name))
        value = input("Enter new value: ")

        for grade in self.finalGrades:
            if(grade.course == theCourse):
                grade.value = value

    def showFinalGrade(self, theCourse):
        for grade in self.finalGrades:
            if(grade.course == theCourse):
                print("Final grade in %s class: %f" %
                      (theCourse.name, grade.value))

    def hasFinalGrade(self, theCourse):
        for grade in self.finalGrades:
            if(grade.course == theCourse):
                return True
        return False
