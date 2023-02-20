from os.path import exists
from Queries import *

def menu():

    filename = input("Qual o caminho para o ficheiro csv? ")

    if(exists(filename)):
        stats(filename)

    else:
        print("Ficheiro não existe.")
        return

    print("\nMENU\n")
    print("1: Mostrar tabela para distribuição da doença por sexo.")
    print("2: Mostrar tabela para distribuição da doença por escalões etários.")
    print("3: Mostrar tabela para distribuição da doença por níveis de colesterol.")
    print("4: Mostrar todas as tabelas.")
    print("5: Mostrar gráficos para distribuição da doença por sexo.")
    print("6: Mostrar gráficos para distribuição da doença por escalões etários.")
    print("7: Mostrar gráficos para distribuição da doença por níveis de colesterol.\n")

    opt = input("Selecione uma opção:")
    print("\n")

    handler = options.get(opt)
    if handler:
        handler()
    else:
        print("Opção inválida")


def handle_option1():
    query1_table()

def handle_option2():
    query2_table()

def handle_option3():
    query3_table()

def handle_option4():
    print_tables()

def handle_option5():
    query1_graph()

def handle_option6():
    query2_graph()

def handle_option7():
    query3_graph()

options = {
    "1": handle_option1,
    "2": handle_option2,
    "3": handle_option3,
    "4": handle_option4,
    "5": handle_option5,
    "6": handle_option6,
    "7": handle_option7
}

menu()

