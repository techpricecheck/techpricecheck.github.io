import gspread
gc = gspread.service_account("../keys.json").open("Price Comparison Form (Responses)")
wks = gc.sheet1.get_all_values()
print(wks)