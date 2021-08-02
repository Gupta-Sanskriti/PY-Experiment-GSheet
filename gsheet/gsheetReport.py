import gspread

gc = gspread.service_account(filename="gspread_creds.json")

# open
worksheet1 = gc.open('worksheet_1').sheet1
worksheet2 = gc.open('worksheet_2').sheet1

print(worksheet1.row_values(1))

heading = worksheet1.row_values(1)
# column2heading = worksheet1.get('B1')
column2heading = heading[1]
print(column2heading)

i = 0
total = 0

for row in range(worksheet1.row_count):
    if str(worksheet1.cell(row+1 ,2).value) == 'olive':
        i = i+ 1
        total = total + (worksheet1.cell(row,1).value)
    else:
        pass

print(i)
print(total)