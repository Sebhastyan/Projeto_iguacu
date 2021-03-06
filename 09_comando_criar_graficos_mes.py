import pandas as pd
import matplotlib.pyplot as plt

#Semelhante ao 8_comando_criar_graficos_ano.py, este codigo criar um gráfico para analisar como está a disposição das amostras obtidas por mês.

# Carregando os dataframes a partir de um arquivo [TIPO]_count.txt obtido em 7_comando_cria_tabelas_estatisticas.py

list_dts = []
f = ".../Chuva_count.txt"

dt = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
n_chuva = len(dt.columns)
dt = dt.sum(axis=1)
dt.columns = ["Chuva"]
list_dts.append(dt)

f = ".../Nivel_count.txt"
dt = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
n_nivel = len(dt.columns)
dt = dt.sum(axis=1)
dt.columns = ["Nivel"]
list_dts.append(dt)

f = ".../Vazao_count.txt"
dt = pd.read_csv(f, sep='\t', index_col=0, parse_dates=True)
n_vazao = len(dt.columns)
dt = dt.sum(axis=1)
dt.columns = ["Vazao"]
list_dts.append(dt)

# Alocando os dataframes em uma lista.

dt = pd.concat(list_dts, axis=1)
dt.columns = ["Chuva", "Nivel", "Vazao"]

fig, ax1 = plt.subplots(figsize=(8, 5))

ax1.set_title('Amostras por mes')
ax1.plot(dt['Chuva'], c='Blue', label='Chuva')
ax1.plot(dt['Nivel'], c='Red', label='Nivel')
ax1.plot(dt['Vazao'], c='Green', label='Vazão')
ax1.set_xlabel('Data')
ax1.set_ylabel('Número de amostras')

# Plotando em retas a quantidade de amostras em cada mês separadas em seus respectivos tipos.

ax2 = ax1.twinx()

ax2.plot(dt['Chuva']/(30.437*n_chuva), '--', c='lightblue', label='Razão Chuva')
ax2.plot(dt['Nivel']/(30.437*n_nivel), '--', c='lightcoral', label='Razão Nivel')
ax2.plot(dt['Vazao']/(30.437*n_vazao), '--', c='lightgreen', label='Razão Vazão')
ax2.set_ylabel('Amostras por mes dividido por número de estações')

# Plotando em pontilhado a quantidade de amostras em cada mês dividido por estações separadas em seus respectivos tipos.

ax2.set_ylim(0, 1)
fig.tight_layout()  

fig.legend(loc='lower left', fontsize=10)

plt.savefig("Grafico_mes.png",dpi=300)
