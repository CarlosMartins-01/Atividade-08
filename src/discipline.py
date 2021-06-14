"""Discipline Class"""


class Discipline:
    def __init__(self, name, discipline_id):
        self.name = name
        self.id = discipline_id

    def __str__(self):
        return 'Nome: ' + str(self.name) + ', Id: ' + str(self.id) + '\n'
