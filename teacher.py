class Teacher:
    def __init__(self, name, discipline, id):
        self.name = name
        self.discipline = discipline
        self.id = id

    def __str__(self):
        return 'Nome: ' + str(self.name) + ', Disciplina: ' + str(self.discipline.name) + ', Id: ' + str(self.id)
