class Grade:

    def __init__(self, course, value, comment, student):
        self.course = course
        self.value = value
        self.comment = comment
        self.student = student

    def toString(self):
        return '{0} {1} {2}'.format(self.course.name, self.value, self.comment)