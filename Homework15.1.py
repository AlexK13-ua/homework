        # 15.1. Виняток користувача

group_limit = 10

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"gender: {self.gender}, age: {self.age}, first name: {self.first_name}, last name: {self.last_name}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, record book: {self.record_book}"

class GroupLimitError(Exception):
    def __init__(self, message = f"В группе не может быть больше {group_limit} студентов"):
        self.message = message
        super().__init__(self.message)

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= group_limit:
            raise GroupLimitError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f'Number:{self.number}\n {all_students} '


gr = Group('PD1')
#  Добавим студентов
for i in range(group_limit):
    st = Student('Male', 20 + i, f'Name_{i}', f'Lastname_{i}', f'RB_{i}')
    gr.add_student(st)

print(f"Сейчас в группе {len(gr.group)} студентов.")

# Добавляем лишнего студента
extra_student = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

try:
    gr.add_student(extra_student)
except GroupLimitError as e:
    print(f"Ошибка: {e}")
