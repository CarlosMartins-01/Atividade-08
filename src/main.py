from src import discipline, teacher
from departament import Departament
from university import University

disciplines = []
disciplines_names = ['Matemática Discreta', 'Fundamentos de Sistemas de Informação', 'Cálculo']

teachers = []
teachers_names = ['Elloá', 'Ricardo', 'Silvia']


def main():
    for i in range(len(disciplines_names)):
        disciplines.append(discipline.Discipline(disciplines_names[i], i + 1))

    for i in range(len(teachers_names)):
        teachers.append(teacher.Teacher(teachers_names[i], disciplines[i], i + 1))

    d1 = Departament('001', 'Computação', teachers)
    d2 = Departament('002', 'Estatística', teachers)
    d3 = Departament('003', 'Geografia', teachers)
    d4 = Departament('004', 'Linguística', teachers)
    d5 = Departament('005', 'Geologia', teachers)

    u1 = University('001', 'UEA', [d1, d2, d3, d4, d5])
    u2 = University('002', 'UFAM', [d1, d2, d3, d4, d5])

    print(u1)
    print(u2)


if __name__ == '__main__':
    main()
