from openpyxl import load_workbook
import os
caminho_correto = os.path.join(
    "C:\\Users\\81035932",
    "OneDrive - Vale S.A",
    "Documents",
    "data",
    "pivot_table.xlsx")

#1- Lê pasta de trabalho e planilha
wb = load_workbook(caminho_correto)
#print(wb)
sheet = wb["Relatorio"]

#2 - Acessando o valor específico

print(sheet["A3"].value)
print(sheet["B3"].value)

#3 - Iterando valores por meio de loop
for i in range(2, 6):
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value
    bt = sheet["C%s" %i].value
    print(f"{ano}) o Aston Martin vendeu {am} e o Bentley vendeu {bt}")
