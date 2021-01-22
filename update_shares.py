from openpyxl import load_workbook

exec(open("convert_csv.py").read())

testWB = load_workbook(filename = 'tester.xlsx')
testSheet = testWB.active

arkgWB = load_workbook(filename = 'arkg_holdings.xlsx') 
arkgSheet = arkgWB.active

sharesWB = load_workbook(filename = 'shareschange.xlsx')
sharesSheet = sharesWB.active


sharesSheet.insert_cols(idx=3)
sharesSheet["C1"] = arkgSheet.cell(row=2, column=1).value

counter = 2 
while counter < arkgSheet.max_row:
    found = False
    stockName = arkgSheet.cell(row=counter, column=3).value
    for cell in sharesSheet['A']:
        if cell.value == stockName:
            sharesSheet.cell(row=cell.row, column=3).value = arkgSheet.cell(row=counter, column=6).value
            found = True
    # add new stock listing to the bottom of the list
    if not found:
        sharesSheet.append({1 : stockName, 2 : arkgSheet.cell(row=counter, column = 4).value, 3:arkgSheet.cell(row=counter, column=6).value})
    counter+=1


sharesWB.save(filename="shareschange.xlsx")

