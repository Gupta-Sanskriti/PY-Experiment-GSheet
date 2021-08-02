import gspread
import pprint

gc = gspread.service_account(filename = 'gspread_creds.json')  #link up the gspread file to this module

sh1 = gc.open_by_key(#google sheet access key)  # opent the file by key
sh2 = gc.open_by_key(#google sheet access key)  #open the seconfd file by key

worksheet1 = sh1.sheet1  #sheet1 is the spreadsheet you are working on .. if still not understood see at the bottom of the spreadsheet
worksheet2 = sh2.sheet1

pp = pprint.PrettyPrinter() #pprint helps us to format the output in an nice manner
res = worksheet1.get_all_records()
# print(worksheet2.get_all_values())
# pp.pprint(res)

# update own row
row = ["9:30 am", "olive", 234]
index = 3
worksheet1.insert_row(row,index)
print(worksheet1.row_count)






