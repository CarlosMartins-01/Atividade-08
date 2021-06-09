class Discipline:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return 'Nome: ' + str(self.name) + ', Id: ' + str(self.id)
