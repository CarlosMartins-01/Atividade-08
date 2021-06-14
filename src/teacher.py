"""Teacher Class"""


class Teacher:
    def __init__(self, name, discipline, teacher_id):
        self.name = name
        self.discipline = discipline
        self.id = teacher_id

    def __str__(self):
        return 'Teacher Name: ' + str(self.name) + ', Discipline: ' + str(self.discipline.name) + ', Id: ' + str(self.id) + '\n'
