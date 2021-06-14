
"""Departament Class"""


class Departament:
    def __init__(self, department_id: str, name: str, teachers: list):
        self.id = department_id
        self.name = name
        self.teachers = teachers
        assert isinstance(self.teachers, list), 'Expected to receive a list of teachers'
        assert 0 < len(teachers) <= 5, 'Add or delete teacher, min:1 and max:5'

    def __str__(self):
        s = ''
        s += 'Departament id: ' + self.id + '\n'
        s += 'Departament name: ' + self.name + '\n'
        for teacher in self.teachers:
            s += teacher.__str__()
        s += '\n'
        return s
