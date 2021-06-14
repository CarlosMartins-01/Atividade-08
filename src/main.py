from discipline import Discipline
from teacher import Teacher
from departament import Departament
from university import University

"""Main"""


def main():
    dc1 = Discipline('Matemática Discreta', '001')
    dc2 = Discipline('Cálculo', '002')

    t1 = Teacher('Elloá', dc1, '001')
    t2 = Teacher('Ricardo', dc2, '002')
    t3 = Teacher('Jucimar jr', dc2, '003')

    teachers = [t1, t2, t3]

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
