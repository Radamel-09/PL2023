estado = False
current_match = ""
matches = []
summ = 0

def handler(texto):

    global estado,current_match,summ

    for char in texto:

        if(estado == True):

            if texto.lower().startswith("off", texto.index(char)):
                estado = False

            elif(char.isdigit()):
                current_match += char

            elif(current_match):
                matches.append(int(current_match))
                current_match = ''
                
            if(char == '='):
                if(not matches): 
                    summ = 0
                summ = sum(matches)
                print(f"Soma = {summ}")

        elif(estado == False):

            if texto.lower().startswith("on", texto.index(char)):
                estado = True

            if(char == '='):
                summ = sum(matches)
                print(f"Soma = {summ}")


def main():

    texto = input("Escreva o seu texto:")

    handler(texto)

main()