class Course:

    def __init__(self, name, id, teacher):
        self.name = name
        self.id = id
        self.students = []
        self.teacher = teacher

    def addStudent(self, student):
        self.students.append(student)

    def showListOfStudents(self):
        i = 1
        for student in self.students:
            print("%d. %s" %(i, student.toString()))
            i += 1