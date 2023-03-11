import re
import os
import json

keys = ["Número","Nome","Curso","Notas","Notas_"]
func = None

def csv_to_list(line):
    aluno_list = re.split(r',', line, maxsplit=3)

    aluno_dict = {}

    for i in range(len(aluno_list)):
        aluno_dict[keys[i]] =  aluno_list[i]
    
    if len(aluno_list) == 4:
        aluno_dict['Notas'] = str_to_list(aluno_list[3]) 

    if func:
        if func=='sum':
            aluno_dict['Notas_'+func] = soma(aluno_list[3])
            del aluno_dict['Notas']
        
        if func=='media':
            aluno_dict['Notas_'+func] = media(aluno_list[3])
            del aluno_dict['Notas']
    
    return aluno_dict


def media(aluno_list):
    
    num_list = str_to_list(aluno_list)

    media_notas = sum(num_list)/len(num_list)

    return media_notas 

def soma(aluno_list):

    num_list = str_to_list(aluno_list)

    soma_notas = sum(num_list)

    return soma_notas

def str_to_list(aluno_list):
    notas_str = aluno_list.split(',')
    return [int(num_str) for num_str in notas_str if num_str]

    
def check_func(first_line):

    global func

    x = re.search(r'::(\w+),',first_line)
    if(x):
        func = x.group(1)
    else:
        func = None

def alunos_to_json(lista_alunos, filename):
    
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(lista_alunos, file, indent=4, separators=(',', ': '), ensure_ascii=False)


def main():     

    lista_alunos = []

    path = input("Qual o caminho para o ficheiro?")

    if(not os.path.exists(path)):
        print("Ficheiro não existe.")
        return
    
    else:
        with open(path) as f:

            first_line = f.readline()
            check_func(first_line)

            content = f.read()

            for line in content.splitlines():
                lista_alunos.append(csv_to_list(line))

            #print (lista_alunos)
            json_file_name = path.replace(".csv", ".json")
            alunos_to_json(lista_alunos,json_file_name)

main()