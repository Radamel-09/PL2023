import os
import sys
from processo import *
import time

def menu():

    path = input("Qual o caminho para o ficheiro?")
    #path = "processos.txt"

    if(not exists(path)):
        print("Ficheiro não existe.")
        return
    
    else:

        print("\nLOADING...\n")

        #start_time = time.time()

        main()

        #end_time = time.time()

        #execution_time = end_time - start_time
        #print("Execution time:", execution_time, "seconds")
        
        while(True):
            
            clear_screen()
            print("\nMENU\n")
            print("1: Mostrar a frequência de processos por ano.")
            print("2: Mostrar a frequência de nomes próprios.")
            print("3: Mostrar a frequência de apelidos.")
            print("4: Mostrar a frequência dos vários tipos de relação.")
            print("5: Converter os 20 primeiros registos num novo ficheiro de output mas em formato Json.")
            print("6: Sair")
            print("\n")

            opt = input("Selecione uma opção:")
            print("\n")

            handler = options.get(opt)
            if handler:
                handler()
                input("\nPressione Enter para continuar...")
            else:
                print("Opção inválida")
                input("\nPressione Enter para continuar...")

def clear_screen():
    if os.name == 'nt': # for Windows
        os.system('cls')
    else: # for Unix/Linux/MacOS
        os.system('clear')

def handle_option1():
    show_frequency()

def handle_option2():
    top_5_names_sec()

def handle_option3():
    top_5_surnames_sec()

def handle_option4():
    show_relacoes()

def handle_option5():
    convert_json()

def handle_option6():
    sys.exit(0)

options = {
    "1": handle_option1,
    "2": handle_option2,
    "3": handle_option3,
    "4": handle_option4,
    "5": handle_option5,
    "6": handle_option6,
}

menu()