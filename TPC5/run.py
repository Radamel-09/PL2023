import re

saldo = (0,0)

moedas = re.compile(r"MOEDA\s(\d+(e|c),\s)*(\d+(e|c))\.")
numeros = re.compile(r"T=(2\d{8}|808\d{6}|800\d{6}$)|T=(00\d{7,13}$)|T=(601\d{6}|604\d{6})$")
abortar = re.compile(r"ABORTAR")

def handler(texto):

    lev = re.compile(r"LEVANTAR")

    while not lev.match(texto):
        print('maq: "Apenas a ação "LEVANTAR" está disponível. Aplique-a para começar as operações"')
        texto = input(">> ")

    if lev.match(texto):
        adicionar_moedas()
        ligar_numero()

def adicionar_moedas():

    input_moeda = input('maq: "Introduza moedas.*Para chamadas verdes faça "MOEDA 0c""\n>> ')
        
    if abortar.match(input_moeda):
        handle_abortar()

    elif (moedas.match(input_moeda)):
        moedas_invalidas_saldo = calculo_saldo(input_moeda)
        if moedas_invalidas_saldo:
            print('maq: "',end = " ")
            print_invalidas(moedas_invalidas_saldo)
            print('- moeda(s) inválida(s); saldo = ' + saldo_to_string(saldo) + '"')
        else:
            print('maq: "Saldo = ' + saldo_to_string(saldo) + '"')
    else:
        adicionar_moedas()

def ligar_numero():

    pousar = re.compile(r"POUSAR")

    input_numero = input('>> ')

    if abortar.match(input_numero):
        handle_abortar()

    if not numeros.match(input_numero):
        print('maq: "Esse número não existe. Queira discar novo número com "T=XXXXXXXXX"!')   
        ligar_numero()

    if numeros.match(input_numero) and numeros.match(input_numero).group(3):
        print('maq: "Esse número não é permitido neste telefone. Queira discar novo número com "T=XXXXXXXXX"!')   
        ligar_numero()

    if numeros.match(input_numero) and not numeros.match(input_numero).group(3):
        print(numeros.match(input_numero).groups())
        check_saldo_suficiente = calculo_numero(input_numero)

        if(check_saldo_suficiente==True):
            ultima_op = input('maq: "saldo = ' + saldo_to_string(saldo) + '"\n>> ')
            while not pousar.match(ultima_op):
                ultima_op = input('maq: "Apenas a ação "POUSAR" está disponível. Após isso pode reiniciar a máquina e fazer as operações que necessita.\n>> ')   
        else: 
            print('maq: "Saldo insuficente: necessita no minimo de ' + check_saldo_suficiente + '."')
            adicionar_moedas()
            ligar_numero()
        troco()
        handle_pousar()


def saldo_to_string(nums):
    return str(nums[0]) + "e" + str(nums[1]) + "c"

def calculo_saldo(input_moedas):

    moeda = moedas.match(input_moedas)
    
    if moeda:
        lista_moedas = re.findall(r"\s(\d+\w),",input_moedas)
        ultima_moeda = re.search(r"\s(\d+\w)\.",input_moedas)
        lista_moedas.append(ultima_moeda.group(1))
        invalidas = validar_moedas(lista_moedas)
    
    return (invalidas)

def validar_moedas(lista_moedas):
    moedas_validas = ["0c","1c","2c","5c","10c","20c","50c","1e","2e"]
    moedas_invalidas = []

    for moeda in lista_moedas:
        if moeda in moedas_validas:
            adicionar_moeda(moeda)
        else:
            moedas_invalidas.append(moeda)

    return moedas_invalidas
    
def adicionar_moeda(moeda):

    global saldo

    saldo_cents = saldo[0]*100 + saldo[1]

    if moeda[-1] == "e":
        moeda = moeda[:-1]
        moeda = int(moeda)
        moeda *= 100 
    
    else:
        moeda = moeda[:-1]
        moeda = int(moeda)
    
    saldo_cents += moeda

    saldo = (int(saldo_cents/100),saldo_cents%100)

def saldo_to_cents(nums):
    return nums[0]*100+nums[1]

def cents_to_saldo(cents):
    return (int(cents/100),cents%100)

def print_invalidas(invalidas):
    print(*invalidas, end=" ")

def calculo_numero(input_numero):

    nacionais = re.compile(r"2\d{8}$")
    #verdes = re.compile(r"800\d{6}$")
    azuis = re.compile(r"808\d{6}$")

    global saldo    
    saldo_necessario = 0
    cents = saldo_to_cents(saldo)

    chamadas = numeros.match(input_numero).group(1)
    
    internacionais = numeros.match(input_numero).group(2)
    
    if chamadas:
        if nacionais.match(chamadas):
            saldo_necessario = 25

        if azuis.match(chamadas):
            saldo_necessario = 10

        if cents >= saldo_necessario: 
            cents -= saldo_necessario
            saldo = cents_to_saldo(cents)
            return True
        else:
            return saldo_to_string(cents_to_saldo(saldo_necessario))
    
    elif internacionais:
        saldo_necessario = 150
        if cents >= saldo_necessario: 
            cents -= saldo_necessario
            saldo = cents_to_saldo(cents)
            return True
        else:
            return saldo_to_string(cents_to_saldo(saldo_necessario))
        
def calculo_final():
    
    return saldo_to_string(saldo) 

def troco(): 
    moedas_troco = saldo_to_cents(saldo)
    moedas_validas = {200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}

    for i in moedas_validas.keys():
        if moedas_troco%i>0 or moedas_troco%i==0:
            moedas_validas[i] = int(moedas_troco/i) 
            moedas_troco -= moedas_validas[i]*i

    list_new_keys = ["2e","1e","50c","20c","10c","5c","2c","1c"]
    new_dict = {}

    for new_key, old_key in zip(list_new_keys, moedas_validas):
        value = moedas_validas[old_key]
        new_dict[new_key] = value

    str_troco = ""
    for j in new_dict.items():
        if j[1] != 0:
            str_troco += " " + str(j[1]) + "x" + j[0] + ","

    str_troco = str_troco[:-1]+";"
    return "; moedas=" + str_troco

def handle_pousar():
    print('maq: "troco= ' + calculo_final() + troco() + ' Volte Sempre!"\n')

def handle_abortar():    
    print('maq: "Recolha as moedas ' + saldo_to_string(saldo) + '."\n')
    exit()
       
def main():

    texto = input(">> ")
    handler(texto)

main()