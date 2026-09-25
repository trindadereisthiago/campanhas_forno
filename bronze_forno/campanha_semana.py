import pandas as pd

caminho = r"Q:\GROUPS\BR_SC_JGS_WMO_METALURGICO_II\07 - FUSÃO\14 - ACOMPANHAMENTO CONFECÇÃO FORNO 30T\2025\Campanhas do Ano - Copia.xlsx"

df_campanhas = pd.read_excel(caminho)

#print("Colunas", df_campanhas.columns.tolist())
#print("\n")
"""
Colunas
['Unnamed: 0', 'Forno', 'Capacidade (ton)', 'Campanha 2024', 'Semana da campanha', 'Data', 'Semana do Ano', 'Quantidade de Refratário']
"""

#print(df_campanhas.head())

df_campanha_silver = df_campanhas[['Forno', 'Campanha 2024', 'Semana da campanha', 'Semana do Ano']]

nome_colunas = {
    'Campanha 2024' : 'Campanha'
}

df_campanhas.replace(nome_colunas)

print(df_campanha_silver.head())

df_campanha_silver.to_excel("silver_forno/campanhas_do_forno.xlsx", index= False)

#print("\n")
#print("Shape", df_campanhas.shape)
#print("\n")
#print("Describe \n", df_campanhas.describe())

#print(df_campanhas.isnull().sum())

#df_campanhas[]