import gspread

gc = gspread.service_account( filename= 'gspread_creds.json')

# OPEN METHOD

# open a sheet from a spreadsheet in on go
wks = gc.open('worksheet_2').sheet1

# you can open a spreadsheet by keys
sht1 = gc.open_by_key(#Gsheet key)

# or, if you feel really lazy to extract that key, paste the entire url
sht2 = gc.open_by_url(#url)


# UPDATE 

# update a range of cell using the top corner addres
wks.update('A1',[[1,2],[3,4]])

# or update a single cell 
# wks.update('B42', "it's doen there somewhere, let me take another look.")

# format the header
wks.format('A1:B1',{'textFormat':{'bold': True}})

# CREATING A SPREADSHEET

sh = gc.create('worksheet_3')

# but that new spreadsheet will be visible only to your script's account
# to be able to access newly created spreadsheet you *must* share it
# with your email. which brings us to ..

# sh.share('21sanskritigupta@gmail.com', perm_type = 'user', role='writer')

# SELECTING A WORKSHEET

# select worksheet by index. worksheet indexes start from zero
worksheet = sh.get_worksheet(0)
print(worksheet)

# by title
# worksheet = sh.worksheet('days') # look after

# most common case:sheet1
worksheet = sh.sheet1

# get a list of all worksheets
worksheet_list = sh.worksheets()

# CREATING A WORKSHEET
worksheet = sh.add_worksheet(title="A worksheet", rows="100", cols="20")  # look after

# DELETING a worksheet
# sh.del_worksheet(worksheet)

#   GETTING A CELL VALUE
# with label
# val = worksheet.get('B1').first()

# with coords
# val = worksheet.cell(1,2).value()

# UPDATING CELLS

# updating a single cell
worksheet.update('B1','Bingo!')

# update a range
worksheet.update('A1:B2',[[1,2],[3,4]])


