from Store import Person, parse_and_store
import matplotlib.pyplot as plt

# Query 1
# Total -> M: 670, F: 169
# temDoenca -> M: 428, F: 40

M = 0
F = 0
DoencaM = 0
DoencaF = 0

# Query 2
# [30-34], [35-39], [40-44], ...
# 21 faixas etárias de 0 até 100+

pessoas_faixas_Doenca = [0] * 21
pessoas_faixas_NDoenca = [0] * 21

# Query 3
# 10 em 10 unidades


def stats():

    pdict = parse_and_store("myheart.csv")

    global M,F,DoencaM,DoencaF,pessoas_faixas

    for key, value in pdict.items():

        #Query 1
        #print(f"temDoenca: {value.temDoenca}, sexo: {value.sexo}")

        if value.sexo == 'M':
            M += 1

            if value.temDoenca == '1':
                DoencaM += 1
                
        if value.sexo == 'F':
            F += 1

            if value.temDoenca == '1':
                DoencaF += 1

        #Query 2

        age = int(value.idade)

        # determine the age range for this person
        age_range = age // 5

        if(value.temDoenca == '1'):
            pessoas_faixas_Doenca[age_range]+= 1
        
        else:
            pessoas_faixas_NDoenca[age_range]+= 1


def query1():

    # Percentagens
    DoencaMPerc = (DoencaM / M) * 100
    DoencaFPerc = (DoencaF / F) * 100

    NoDoencaMPerc = 100 - DoencaMPerc
    NoDoencaFPerc = 100 - DoencaFPerc

    # Plot pie charts
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,6))
    fig.suptitle("Distribuição da Doença por sexo", fontsize=16)

    # Pie chart Masculino
    ax1.pie([DoencaM, M-DoencaM], labels=["tem Doença", "Não tem Doença"], autopct='%.2f%%', colors=["tab:orange", "tab:blue"])
    ax1.set_title(f"Masculino (Total: {M})\nDoença: {DoencaM} | Não tem Doença: {M-DoencaM}")

    # Pie chart Feminino
    ax2.pie([DoencaF, F-DoencaF], labels=["tem Doença", "Não tem Doença"], autopct='%.2f%%', colors=["tab:orange", "tab:blue"])
    ax2.set_title(f"Feminino (Total: {F})\nDoença: {DoencaF} | Não tem Doença: {F-DoencaF}")

    plt.show()


    m = ('M', DoencaM, round(DoencaMPerc, 2))
    f = ('F', DoencaF, round(DoencaFPerc, 2))

    return (m,f)

def query2():

    age_labels = ['0-4', '5-9', '10-14', '15-19', '20-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80-84', '85-89', '90-94', '95-99', '100+']

    fig, ax = plt.subplots()

    # Set the x-axis ticks and labels
    x_pos = [i for i in range(len(age_labels))]
    ax.set_xticks(x_pos)
    ax.set_xticklabels(age_labels, rotation=90)

    # Set the y-axis and x-axis label
    ax.set_ylabel('Número de Pessoas')
    plt.xlabel('Faixas etárias')
    

    # Create the bar plots for Doenca and NDoenca
    ax.bar(x_pos, pessoas_faixas_Doenca, align='center', alpha=0.5, label='Doenca')
    ax.bar(x_pos, pessoas_faixas_NDoenca, align='center', alpha=0.5, label='NDoenca', bottom=pessoas_faixas_Doenca)

    # Add a legend
    ax.legend()

    # Set the title of the graph
    ax.set_title('Número de pessoas com e sem a Doença por faixa etária')

    plt.xlabel('Faixas etárias')

    # Show the graph
    plt.show()


def main():

    stats()
    #print(query1())
    print(query2())

main()