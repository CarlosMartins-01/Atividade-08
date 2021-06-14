from discipline import Discipline
from teacher import Teacher
from departament import Departament
from university import University

"""Main"""


def main():
    dc1 = Discipline('Matemática Discreta', '001')
    dc2 = Discipline('Cálculo', '002')
    dc3 = Discipline('Banco de Dados', '003')

    t1 = Teacher('Elloá', dc1, '001')
    t2 = Teacher('Ricardo', dc2, '002')
    t3 = Teacher('Jucimar jr', dc2, '003')
    t4 = Teacher('Cleber', dc3, '003')
    t5 = Teacher('Hellen', dc3, '003')

    teachers = [t1, t2, t3, t4, t5]

    d1 = Departament('001', 'Computação', teachers[:3])
    d2 = Departament('002', 'Estatística', teachers[2:])
    d3 = Departament('003', 'Geografia', teachers[:4])
    d4 = Departament('004', 'Linguística', teachers[:2])
    d5 = Departament('005', 'Geologia', teachers[0:1])

    u1 = University('001', 'UEA', [d1, d2, d3, d4, d5])
    u2 = University('002', 'UFAM', [d1, d2, d5])
    #u3 = University('002', 'DEBUG UNIVERSITY', [d1, d2, d5, d3, d4, d5, d1])
    loop = True
    while(loop):
        print()
        print()
        print("--- 2 Universidades Cadastradas ----")
        selected_univ = input("1 - " + u1.name + "\n2 - " + u2.name + "\n3 - Sobre" + "\nDigite o número que deseja visualizar:")

        if  selected_univ == '1':
            print()
            print("-----------------------------------------------------------------------")
            print(u1)
        elif selected_univ == '2':
            print("-----------------------------------------------------------------------")
            print(u2)
        elif selected_univ == '3':
            print("-----------------------------------------------------------------------")
            print("Desenvolvedores:")
            print("- Carlos Martins\n- Daniele Simas\n- Dayvson Silva\n- Diógeles Tamaturgo\n- Elikson Tavares")
        else:
            print("selecione um valor válido")
        contin = input("\nDeseja continuar? (s/n):")
        if not contin == 's':
            loop = False

if __name__ == '__main__':
    main()
