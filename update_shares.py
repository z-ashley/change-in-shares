from openpyxl import load_workbook

testWB = load_workbook(filename = 'tester.xlsx')
testSheet = testWB.active

arkgWB = load_workbook(filename = 'arkg_holdings1.xlsx')
arkgSheet = arkgWB.active

sharesWB = load_workbook(filename = 'shareschange.xlsx')
sharesSheet = sharesWB.active


counter = 1
for row in sharesSheet.iter_rows(1):
    stockName = arkgSheet.cell(row=counter, column=3).value
    for cell in row:
        if cell.value == stockName:
            sharesSheet.cell(row=cell.row, column=3).value = arkgSheet.cell(row=counter, column=6).value
    counter+=1

sharesWB.save(filename="shareschange.xlsx")