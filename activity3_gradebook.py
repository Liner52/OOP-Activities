class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score


class Gradebook:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def get_average(self):
        if len(self.students) == 0:
            return 0

        total = 0
        for student in self.students:
            total += student.score

        return total / len(self.students)
