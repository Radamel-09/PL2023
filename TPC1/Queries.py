from Store import Person, parse_and_store
import matplotlib.pyplot as plt
from tabulate import tabulate

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

faixas_etarias = []
for i in range(0, 101, 5):
    if i < 100:
        label = f"{i}-{i+4}"
    else:
        label = "100+"
    faixas_etarias.append(label)


pessoas_faixas_Doenca = [0] * 21
pessoas_faixas_NDoenca = [0] * 21

# Query 3
# 10 em 10 unidades

int_col = []
for i in range(0, 605, 10):
    if i < 605:
        label = f"{i}-{i+9}"

    int_col.append(label)

pessoas_col_Doenca = [0] * 61
pessoas_col_NDoenca = [0] * 61


def stats(path):

    pdict = parse_and_store(path)

    global M,F,DoencaM,DoencaF,pessoas_faixas,pessoas_col_Doenca,pessoas_col_NDoenca

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

        #Query 3

        col = int(value.colesterol)

        col_range = col // 10

        if(value.temDoenca == '1'):
            pessoas_col_Doenca[col_range]+= 1
        
        else:
            pessoas_col_NDoenca[col_range]+= 1


def query1_graph():

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


def query1_table():

    NoDoencaM = M-DoencaM
    NoDoencaF = F-DoencaF
    
    table = [["Sexo","Com Doença","Sem Doença","Total"],["Masculino",DoencaM,NoDoencaM,M],
             ["Feminino",DoencaF,NoDoencaF,F],["Total",DoencaM+DoencaF,NoDoencaM+NoDoencaF,M+F]]
    
    print("Distribuição da Doença por sexo")
    print(tabulate(table, tablefmt = 'fancy_grid'))
    
    return table

def query2_graph():

    fig, ax = plt.subplots()

    # Set the x-axis ticks and labels
    x_pos = [i for i in range(len(faixas_etarias))]
    ax.set_xticks(x_pos)
    ax.set_xticklabels(faixas_etarias, rotation=90)

    # Set the y-axis and x-axis label
    ax.set_ylabel('Número de Pessoas')
    plt.xlabel('Faixas etárias')
    

    # Create the bar plots for Doenca and NDoenca
    ax.bar(x_pos, pessoas_faixas_Doenca, align='center', alpha=0.5, label='Doenca')
    ax.bar(x_pos, pessoas_faixas_NDoenca, align='center', alpha=0.5, label='NDoenca', bottom=pessoas_faixas_Doenca)

    # Add a legend
    ax.legend()

    # Set the title of the graph
    ax.set_title('Distribuição da doença pela faixa etária')

    plt.xlabel('Faixas etárias')

    # Show the graph
    plt.show()

def query2_table():

    table = [["Faixa etária", "Com Doença", "Sem Doença", "Total"]]

    for faixa in faixas_etarias:
        idx = faixas_etarias.index(faixa)
        total = pessoas_faixas_Doenca[idx] + pessoas_faixas_NDoenca[idx]
        linha = [faixa, pessoas_faixas_Doenca[idx], pessoas_faixas_NDoenca[idx], total]
        table.append(linha)
    
    print("Distribuição da doença pela faixa etária")
    print(tabulate(table, tablefmt = 'fancy_grid'))

    return table

def query3_graph():

    fig, ax = plt.subplots()

    # Set the x-axis ticks and labels
    x_pos = [i for i in range(len(int_col))]
    ax.set_xticks(x_pos)
    ax.set_xticklabels(int_col, rotation=90)

    # Set the y-axis and x-axis label
    ax.set_ylabel('Número de Pessoas')
    plt.xlabel('Colesterol')
    

    # Create the bar plots for Doenca and NDoenca
    ax.bar(x_pos, pessoas_col_Doenca, align='center', alpha=0.5, label='Doenca')
    ax.bar(x_pos, pessoas_col_NDoenca, align='center', alpha=0.5, label='NDoenca', bottom=pessoas_col_Doenca)

    # Add a legend
    ax.legend()

    # Set the title of the graph
    ax.set_title('Distribuição da doença pelos valores de colesterol')

    plt.xlabel('Colesterol')

    # Show the graph
    plt.show()

def query3_table():

    table = [["Colesterol", "Com Doença", "Sem Doença", "Total"]]

    for col in int_col:
        idx = int_col.index(col)
        total = pessoas_col_Doenca[idx] + pessoas_col_NDoenca[idx]
        linha = [col, pessoas_col_Doenca[idx], pessoas_col_NDoenca[idx], total]
        table.append(linha)
    
    print("Distribuição da doença pelos valores de colesterol")
    print(tabulate(table, tablefmt = 'fancy_grid'))

    return table

def print_tables():

    query1_table()
    query2_table()
    query3_table()

def show_graphs():

    query1_graph()
    query2_graph()
    query3_graph()

def main():

    stats("myheart.csv")
    
    print_tables()
    show_graphs()

main()
