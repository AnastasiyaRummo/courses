# from student import Student


class CourseGroup:

    def __init__(self, student, classmates):
        self.st = student
        self.cl = classmates

    def __str__(self):
        classmates_str = ", ".join([str(classmate) for classmate in self.cl])
        return f"{self.st} учится вместе с: {classmates_str}"

# class CourseGroup:
#     def __init__(self, student, classmates):
#         self.student = student
#         self.classmates = classmates  # Список объектов класса Student
#
#     def __str__(self):
#         classmates_str = ""
#         for classmate in self.classmates:
#             if classmate != self.student:
# Проверка, чтобы не включать самого студента

#                 if classmates_str:
#                     classmates_str += ", "
#                 classmates_str += str(classmate)
#         return f"{self.student} учится вместе с: {classmates_str}"
