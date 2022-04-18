import pandas as pd
import numpy as np

'''folders = [".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Anual/Vazao_count.txt",
     ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Anual/Chuva_count.txt",
     ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Anual/Nivel_count.txt"]'''

folders = ["/home/seb/Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Mensal/Vazao_count.txt",
     ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Mensal/Chuva_count.txt",
     ".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Estatisticas/Mensal/Nivel_count.txt"]

#dir_save="/home/seb/Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Analise-periodo-comum/Anuais/"
dir_save=".../Projeto-iguacu/Dados_Processados_Sem_Duplicidades/Analise-periodo-comum/Mensais/"

percs = np.arange(0.1, 1, 0.1)

for f in folders:
    dt = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
    #dt = dt/365
    dt = dt/30.437 

    tipo = f.split('/')[-1][:-10]
    dir_save_novo = str(dir_save+tipo+'/')

    for perc in percs:
        dt_pivot = dt.copy()

        mask = (dt_pivot <= perc)
        dt_pivot[mask] = np.nan
        dt_pivot[~mask] = 'x'
        
        dt_pivot.to_csv(dir_save_novo + tipo + '_' + str((perc*100).round(0)) + '%.txt', sep='\t')
