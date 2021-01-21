# converts the downloaded csv to xlsx

import csv
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active

with open('arkg_holdings.csv') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        ws.append(row)

wb.save('arkg_holdings1.xlsx')