from os.path import exists
import re

matches = lines = 0
frequency_dict = {}
names_dict = {}
surnames_dict = {}
relacoes_dict = {}
json_reg = []

def frequency(line):

    global matches,lines,frequency_dict

    x = re.match(r"(?P<pasta>\d+)::(?P<ano>[0-9]{4})-(?P<mes>[0-9]{2})-(?P<dia>[0-9]{2})::(?P<nome>[\w\s.]+)::(?P<pai>.*)::(?P<mae>.*)::(?P<extras>.*)::", line)

    if(x):
        #frequência por ano
        year = int(x.group('ano'))
        if year in frequency_dict:
            frequency_dict[year] += 1
        else:
            frequency_dict[year] = 1

        #nomes e apelidos
        tuple = get_name_and_surname(year // 100 + 1,x.group('nome'))
        add_top_names(tuple)
        add_top_surnames(tuple)
        
        #relações
        if(x.group('extras')):
            get_relacoes(line)

        #json 
        if(lines<20):
            line_dict = {"pasta":x.group('pasta'),"data":x.group('ano') + "-" + x.group('mes') + "-" + x.group('dia'),"nome":x.group('nome'),"pai":x.group('pai'),"mae":x.group('mae'),"extras":x.group('extras')}
            json_reg.append(line_dict)
            lines += 1

        #37880
        matches += 1


def show_frequency():
    sorted_dict = {k: frequency_dict[k] for k in sorted(frequency_dict)}
    print(sorted_dict)   

def get_name_and_surname(seculo, name):
    names = name.split(' ')
    return (seculo,names[0], names[-1])

#example_dict = {seculo: [('nome1',frequency1), ('nome2',frequency2)]}
#tuple(seculo,nome,apelido)

def add_top_names(ntuple):

    global names_dict

    key = ntuple[0]
    name = ntuple[1]

    if key in names_dict:
        name_list = names_dict[key]
        for i, (curr_name, freq) in enumerate(name_list):
            if (curr_name == name):

                name_list[i] = (curr_name, freq+1)

                break
        else:
            name_list.append((name, 1))

        name_list.sort(key=lambda x: x[1],reverse=True)

    else:
        names_dict[key] = [(name, 1)]
        name_list = [(name, 1)]

    
def add_top_surnames(ntuple):

    global surnames_dict

    key = ntuple[0]
    name = ntuple[2]

    if key in surnames_dict:
        name_list = surnames_dict[key]
        for i, (curr_name, freq) in enumerate(name_list):
            if (curr_name == name):

                name_list[i] = (curr_name, freq+1)

                break
        else:
            name_list.append((name, 1))

        name_list.sort(key=lambda x: x[1],reverse=True)

    else:
        surnames_dict[key] = [(name, 1)]
        name_list = [(name, 1)]



def top_5_names_sec():

    for key, name_list in names_dict.items():
        names_dict[key] = name_list[:5]

    sorted_dict = {k: names_dict[k] for k in sorted(names_dict)}

    for key, name_list in sorted_dict.items():
        print("{}: ".format(key))
        for name, freq in name_list:
            print("  {} ({})".format(name, freq))

def top_5_surnames_sec():

    for key, name_list in surnames_dict.items():
        surnames_dict[key] = name_list[:5]

    sorted_dict = {k: surnames_dict[k] for k in sorted(surnames_dict)}
    
    for key, surname_list in sorted_dict.items():
        print("{}: ".format(key))
        for name, freq in surname_list:
            print("  {} ({})".format(name, freq))

def get_relacoes(line):

    global relacoes_dict

    matches = re.findall(r"(?:[A-Z][a-z]+),([A-Z][\w\s]+)\.",line)

    if matches:
        for match in matches:
            if match in relacoes_dict:
                relacoes_dict[match] += 1

            else:
                relacoes_dict[match] = 1
        

def show_relacoes():
    sorted_dict = dict(sorted(relacoes_dict.items(), key=lambda x: x[1], reverse=True))
    print(sorted_dict)

def convert_json():
    new_reg = str(json_reg).replace("'", '"')
    print(new_reg)
        

def main(path):

    if(not exists(path)):
        print("Ficheiro não existe.")
        return
    
    else:

        with open(path) as f:

            content = f.read()

            for line in content.splitlines():
                frequency(line)

    #print(matches)
  