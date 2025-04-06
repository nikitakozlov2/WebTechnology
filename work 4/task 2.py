import csv
from openpyxl import Workbook

with open("Book.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=',')
    data = list(reader)

wb = Workbook()
ws = wb.active

for i, row in enumerate(data):
    if i == 0:
        ws.append(row)
    else:
        row[2] = row[2] + ' руб.'
        row[3] = row[3] + ' руб.'
        ws.append(row)

wb.save("NewBook.xlsx")