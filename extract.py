import pandas as pd

url_producao_qualidade = 'https://raw.githubusercontent.com/trindadereisthiago/campanhas_forno/main/bronze_forno/dados_producao.xlsx'

url_producao_sfm = 'https://raw.githubusercontent.com/trindadereisthiago/campanhas_forno/main/bronze_forno/producao_met_1.xlsx'

url_materiais_ordens = 'https://raw.githubusercontent.com/trindadereisthiago/campanhas_forno/main/bronze_forno/materiais_ordens2.XLSX'

df_producao_qualidade = pd.read_excel(url_producao_qualidade)

df_producao_sfm = pd.read_excel(url_producao_sfm)

df_materiais_ordens = pd.read_excel(url_materiais_ordens)

print(df_producao_qualidade.head())

print(df_producao_sfm.head())

print(df_materiais_ordens.head())
