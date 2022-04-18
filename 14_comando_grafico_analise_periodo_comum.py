import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cont = ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Anual/Nivel_count.txt"
cont = ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Anual/Vazao_count.txt"

#f=".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Analise-periodo-comum/Rio_Principal/Estacoes_Rio_Principal_Nivel.txt"
f=".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Analise-periodo-comum/Rio_Principal/Estacoes_Rio_Principal_Vazao.txt"

dir_save=".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Analise-periodo-comum/Rio_Principal/"

lista = pd.read_csv(f, sep='\t', index_col=0, header=[0])

dt = pd.read_csv(cont, sep='\t', index_col=0, parse_dates=True)

list_dts = []
list_erros = []
for i in range(len(lista)):
    cod = str(lista.index[i])
    try:
        aux = dt.loc[:,cod]
        list_dts.append(aux)
    except:
        list_erros.append(cod)

dt2 = pd.concat(list_dts, axis=1)

dt2 = dt2/365

tipo = cont.split('/')[-1][:-10]

# dir_save_novo = str(dir_save + '/')
dir_save_novo = dir_save

percs = np.arange(0.1, 1, 0.1)

for perc in percs:
    dt_pivot = dt2.copy()
    dt_pivot2 = dt2.copy()

    mask = (dt_pivot <= perc)
    dt_pivot2[mask] = np.nan
    dt_pivot2[~mask] = 'x'
    #dt_pivot2.to_csv(dir_save_novo + tipo + '_' + str((perc*100).round(0)) + '%.txt', sep='\t')

    dt_pivot[mask] = np.nan
    dt_pivot[~mask] = 1
    aux=1

    for i in range(len(dt2.columns)):
        cod = dt2.columns[i]
        dt_pivot[cod] = dt_pivot[cod]*aux
        aux = aux+1

    fig, ax1 = plt.subplots(figsize=(10, 9))

    #dt_pivot.plot(ax=ax1, c='orange', lw=5, legend=None)
    dt_pivot.plot(ax=ax1, c='dodgerblue', lw=5, legend=None)

    plt.yticks(np.arange(1, len(dt_pivot.columns)+1, 1), dt_pivot.columns, size='small')

    ax1.set_ylim(0+0.5, len(dt_pivot.columns)+0.5)
    plt.grid(True)

    plt.xlabel('Ano')
    plt.ylabel('Código da Estação')

    plt.tight_layout()

    #plt.savefig(dir_save_novo + tipo + '_' + str((perc*100).round(0)) + '%.pdf', format = 'pdf')
    plt.savefig(dir_save_novo + tipo + '_' + str((perc*100).round(0)) + '%.png', format = 'png')

    plt.close()
