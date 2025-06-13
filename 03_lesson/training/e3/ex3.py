from student import Student
from group import CourseGroup

student = Student('Железный', 'Человек', 30, 'Мстители')
classmates1 = Student('Зеленый', 'Халк', 33, 'Мстители')
classmates2 = Student('Капитан', 'Америка', 31, 'Мстители')
classmates3 = Student('Черная', 'Вдова', 30, 'Мстители')

my_courseGroup = CourseGroup(student, [classmates1, classmates2, classmates3])
print(my_courseGroup)
