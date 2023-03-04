from os.path import exists
from processo import *

def menu():

    #path = input("Qual o caminho para o ficheiro?")
    path = "processos copy.txt"

    if(not exists(path)):
        print("Ficheiro não existe.")
        return
    
    else:

        main()

        print("\nMENU\n")
        print("1: Mostrar a frequência de processos por ano.")
        print("2: Mostrar a frequência de nomes próprios.")
        print("3: Mostrar a frequência de apelidos.")
        print("4: Mostrar a frequência dos vários tipos de relação.")
        print("5: Converter os 20 primeiros registos num novo ficheiro de output mas em formato Json.")
        print("\n")

        opt = input("Selecione uma opção:")
        print("\n")

        handler = options.get(opt)
        if handler:
            handler()
        else:
            print("Opção inválida")


def handle_option1():
    show_frequency()

def handle_option2():
    top_5_names_sec()

def handle_option3():
    top_5_surnames_sec()

def handle_option4():
    print("not done")

def handle_option5():
    print("not done")

options = {
    "1": handle_option1,
    "2": handle_option2,
    "3": handle_option3,
    "4": handle_option4,
    "5": handle_option5,
}

menu()