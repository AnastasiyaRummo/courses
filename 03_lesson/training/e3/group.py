from student import Student


class CourseGroup:

    def __init__(self, student, classmates):
        self.st = student
        self.cl = classmates

    def __str__(self):
        classmates_str = ", ".join([str(classmate) for classmate in self.cl])
        return f"{self.st} учится вместе с: {classmates_str}"
