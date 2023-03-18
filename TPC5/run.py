import re

saldo = (0,0)

def handler(texto):

    lev = re.compile(r"LEVANTAR")
    pousar = re.compile(r"POUSAR")
    abortar = re.compile(r"ABORTAR")
    numeros = re.compile(r"T=(\d{9})")
    moedas = re.compile(r"MOEDA\s(\d+\w,\s*)+(\d+\w)\.")

    while not lev.match(texto):
        print('maq: "Apenas a ação "LEVANTAR" está disponível. Aplique-a para começar as operações"')
        texto = input(">> ")

    if lev.match(texto):
        input_moeda = input('maq: "Introduza moedas."\n>> ')
        
        if abortar.match(input_moeda):
            handle_abortar()

        else:
            moedas_invalidas_saldo = calculo_saldo(input_moeda)
            if moedas_invalidas_saldo:
                print('maq: "',end = " ")
                print_invalidas(moedas_invalidas_saldo)
                print('- moeda(s) inválida(s); saldo = ' + saldo_to_string(saldo) + '"')
            else:
                print('maq: "Saldo = ' + saldo_to_string(saldo) + '"')
            
            input_numero = input('>> ')

            if abortar.match(input_numero):
                handle_abortar()

            #fazer opção para inserir mais moedas
            
            while not numeros.match(input_numero):
                numero_errado = input('maq: "Esse número não é permitido neste telefone. Queira discar novo número com "T=XXXXXXXXX"!\n>> ')   
                if abortar.match(numero_errado):
                    handle_abortar()

            if numeros.match(input_numero):
                ultima_op = input('maq: "saldo = ' + saldo_to_string(saldo) + '"\n>> ')
                while not pousar.match(ultima_op):
                    ultima_op = input('maq: "Apenas a ação "POUSAR" está disponível. Após isso pode reiniciar a máquina e fazer as operações que necessita.\n>> ')   
                
                handle_pousar()


def saldo_to_nums(texto):
    nums = re.match(r'(\d+)e(\d+)c',texto)
    return (nums.group(1),nums.group(2)) 

def saldo_to_string(nums):
    return str(nums[0]) + "e" + str(nums[1]) + "c"

def calculo_saldo(input_moedas):

    moeda = re.match(r"MOEDA\s(\d+\w,\s)+(\d+\w)\.",input_moedas)
    
    if moeda:
        moedas = re.findall(r"\s(\d+\w),",input_moedas)
        ultima_moeda = re.search(r"\s(\d+\w)\.",input_moedas)
        moedas.append(ultima_moeda.group(1))
        invalidas = validar_moedas(moedas)
    
    return (invalidas)

def validar_moedas(lista_moedas):
    moedas_validas = ["1c","2c","5c","10c","20c","50c","1e","2e"]
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

def saldo_to_cents():
    return saldo[0]*100+saldo[1]

def print_invalidas(invalidas):
    print(*invalidas, end=" ")

def calculo_numero(input_numero):
    print("not done")
    return 0

def calculo_final():
    
    return saldo_to_string(saldo) 

def handle_pousar():
    print('maq: "troco=' + calculo_final() + '; Volte Sempre!"\n')

def handle_abortar():    
    print('maq: "Recolha as moedas ' + saldo_to_string(saldo) + '."\n')
    exit()
       
def main():

    texto = input(">> ")
    handler(texto)

main()