import pandas as pd
import os

def Dataframe_from_txt_Hidroweb_RESUMO_DESCARGA(filename):

    dt = pd.read_csv(filename, sep="\t|;", header=[6], engine='python', decimal=",")

    dt.columns = ['NivelConsistencia', 'Data', 'Hora', 'NumMedicao', 'Cota', 'Vazao', 'AreaMolhada', 'Largura',
                   'VelMedia', 'Profundidade', 'datains', 'dataalt', 'respalt', 'tecnico', 'medidorvazao',
                   'algumacoisa']

    dt = dt[['NivelConsistencia', 'Data', 'Hora', 'Cota', 'Vazao', 'AreaMolhada', 'Largura', 'VelMedia', 'Profundidade']]

    dt['Data'] = pd.to_datetime(dt['Data'] + ' ' + dt['Hora'].str.replace('01/01/1900 ', ''), format='%d/%m/%Y %H:%M:%S')

    del dt['Hora']

    dt = dt.set_index('Data')

    return dt

folder=".../Projeto-iguacu/Estacoes/Resumo_Descarga_Bruto"

dir_save=".../Projeto-iguacu/Estacoes/Resumo_Descarga_Processado"

for f in os.listdir(folder):
    file = f'{folder}/{f}'
    save = f'{dir_save}/{f}'
    dt = Dataframe_from_txt_Hidroweb_RESUMO_DESCARGA(file)

    dt.to_csv(save, sep='\t')
