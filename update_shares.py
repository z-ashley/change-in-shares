from openpyxl import load_workbook
arkgWB = load_workbook(filename = 'arkg_holdings1.xlsx')
arkgSheet = arkgWB.active

sharesWB = load_workbook(filename = 'shareschange.xlsx')
sharesSheet = sharesWB.active

print(arkgSheet.max_row)

# for rowNum in range(1, arkgSheet.max_row): 
#     sharesSheet.cell(row=rowNum, column=1).value = arkgSheet.cell(row=rowNum, column=1).value