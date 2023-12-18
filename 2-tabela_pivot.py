import pandas as pd

#1 - Importando Dados

data = pd.read_excel("/data/VendaCarros.xlsx")

#Visualizando o arquivo
#print(data)
#nome = 'Rodrigo'
#print(type('data'))

# 2 - Selecionando colunas específicas do dataframe
df = data[["Fabricante", "ValorVenda", "Ano"]]
print(df)

#3 - Criando a tabela pivot
pivot_table = df.pivot_table(
    values="ValorVenda",
    index='Ano',
    columns='Fabricante',
    aggfunc="sum"
)

print(pivot_table)

#Exportando tabela pivot em arquivo excel
pivot_table.to_excel("PivotTable.xlsx", "Relatorio")

