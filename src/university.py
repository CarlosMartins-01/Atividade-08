class University:
    def __init__(self, university_id: str, name: str, departments: list):
        self.id = university_id
        self.name = name
        self.departments = departments
        assert isinstance(self.departments, list), 'Expected to receive a list of departments'
        assert 0 < len(self.departments) <= 5, 'Add or delete departament, min:1 and max:5'

    def __str__(self):
        s = ''
        s += 'University id :' + self.id + '\n'
        s += 'University Name: ' + self.name + '\n\n'
        for department in self.departments:
            s += department.__str__()
        s += '\n'
        return s

    def add_departament(self, department):
        if 0 > len(self.departments) <= 5:
            self.departments.append(department)
        else:
            print('Is not possible add more departament')
