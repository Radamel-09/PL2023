class Person:
# idade,sexo,tensão,colesterol,batimento,temDoença

    def __init__(self,idade: int,sexo: str,tensao: int,colesterol: int,batimento: int,temDoenca: int):

        self.idade = idade
        self.sexo = sexo
        self.tensao = tensao
        self.colesterol = colesterol
        self.batimento = batimento
        self.temDoenca = temDoenca


def parse_and_store(path):

    persons_dict = {}

    with open(path) as f:

        next(f)

        content = f.read()

        for line in content.splitlines():
            data = line.strip().split(',')
            idade, sexo, tensao, colesterol, batimento, temDoenca = data[:6]

            person = Person(idade, sexo, tensao, colesterol, batimento, temDoenca)

            persons_dict[id(person)] = person
    
    return persons_dict


