import pandas as pd

# 1- Importando dados
data = pd.read_excel("/data/VendaCarros.xlsx")

#Visualizando o arquivo
print(data)

# 2- Lista os primeiros registros
print(data.head())

#3- Lista os últimos registros
print(data.tail()) 


#4 - Quantidade de valores por Fabricantes 
print(data["Fabricante"].value_counts())

