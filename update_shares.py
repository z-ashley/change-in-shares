from openpyxl import load_workbook

testWB = load_workbook(filename = 'tester.xlsx')
testSheet = testWB.active

arkgWB = load_workbook(filename = 'arkg_holdings2.xlsx')
arkgSheet = arkgWB.active

sharesWB = load_workbook(filename = 'shareschange.xlsx')
sharesSheet = sharesWB.active


sharesSheet.insert_cols(idx=3)

counter = 1 
while counter < arkgSheet.max_row:
    stockName = arkgSheet.cell(row=counter, column=3).value
    for cell in sharesSheet['A']:
        if cell.value == stockName:
            sharesSheet.cell(row=cell.row, column=3).value = arkgSheet.cell(row=counter, column=6).value
    counter+=1

del

sharesWB.save(filename="shareschange.xlsx")

