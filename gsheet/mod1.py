import gspread

gc = gspread.service_account(filename = 'gspread_creds.json')
sh = gc.open_by_key(#credential key of gsheel)

worksheet = sh.sheet1

# res = worksheet.get_all_records()  # this prints our all the key value pairs
# res = worksheet.get_all_values()   # this prints out our all the values only
# res = worksheet.row_values(1) #gives the row value
# res = worksheet.col_values(1) #gives the column value
# res =  worksheet.get('A1')  #gets the value of any coloumn
# res = worksheet.get('A2:C23')  # we can specify the range too

# to insert a row with values
user = ["susan", 25,"sydney"]
# worksheet.insert_row(user, 3) # we need to specify the row
# worksheet.append_row(user)

# update specific cell value update_cell(row,col,update item)
worksheet.update_cell(6,2,28)

# delete cell
worksheet.delete_row(1)

# to insert the coloumn with values

# print(res)
