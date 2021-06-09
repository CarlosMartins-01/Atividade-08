import discipline
import teacher

disciplines = []
disciplines_names = ['Matemática Discreta', 'Fundamentos de Sistemas de Informação', 'Cálculo']

teachers = []
teachers_names = ['Elloá', 'Ricardo', 'Silvia']


def main():
    for i in range(len(disciplines_names)):
        disciplines.append(discipline.Discipline(disciplines_names[i], i + 1))

    for i in range(len(teachers_names)):
        teachers.append(teacher.Teacher(teachers_names[i], disciplines[i], i + 1))
 
    print('Disciplinas')
    for i in range(len(disciplines)):
        print(disciplines[i].__str__())

    print('\nProfessores')
    for i in range(len(teachers_names)):
        print(teachers[i].__str__())


main()
