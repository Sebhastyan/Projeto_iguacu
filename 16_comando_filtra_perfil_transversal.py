import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

def Dataframe_from_txt_Hidroweb_PERFIL_TRANSVERSAL(filename):

    list_dts = []
    with open(filename, errors="ignore") as f:
        for i, line in enumerate(f):
            if i > 11:
                line = line.replace('|', '')
                line = line.replace(',', '.')
                tudo = line.split(";")[1:]

                if tudo[2] != '':
                    horas = datetime.strptime(tudo[2], '%d/%m/%Y %H:%M:%S')
                    date = datetime.strptime(tudo[1], '%d/%m/%Y') + timedelta(hours=horas.hour, minutes=horas.minute, seconds=horas.second)
                else:
                    date = datetime.strptime(tudo[1], '%d/%m/%Y').date()

                # Exclue a data e hora, pq já foi guardada em outra variável
                tudo.pop(1)
                tudo.pop(1)

                tudo[-1] = tudo[-1].strip()

                complemento = tudo[:11]

                n_verticais = int(complemento[3])
                verticais = tudo[-n_verticais * 2 - 1:-1]

                distancias = np.array(verticais[0:][::2], dtype=np.float32)
                profundidades = np.array(verticais[1:][::2], dtype=np.float32)
                # Só separa se tiver dados

                nomes = ['Data', 'NivelConsistencia', 'NumLevantamento', 'TipoSecao', 'NumVerticais', 'DistanciaPIPF', 'EixoXDistMaxima', 'EixoXDistMinima', 'EixoYCotaMaxima', 'EixoYCotaMinima', 'ElmGeomPassoCota', 'Observacoes', '']
                dados = [[date]] + [[i] for i in complemento] + [['Distancia', 'Profundidade']]

                index = pd.MultiIndex.from_product(dados, names=nomes)
                dt_comp = pd.DataFrame([distancias, profundidades], index=index)
                dt_comp.columns = 'Medida ' + dt_comp.columns.astype(str)
                list_dts.append(dt_comp)

    dt = pd.concat(list_dts, axis=0).T.sort_index(axis=1)

    return dt.round(2)


folder=".../Projeto-iguacu/Estacoes/Perfil_Transversal_Bruto"

dir_save=".../Projeto-iguacu/Estacoes/Perfil_Transversal_Processado"

for f in os.listdir(folder):
    file = f'{folder}/{f}'
    save = f'{dir_save}/{f}'
    dt = Dataframe_from_txt_Hidroweb_PERFIL_TRANSVERSAL(file)

    dt.to_csv(save, sep='\t')
