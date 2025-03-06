import gspread
import random
arr = list("abcdefghijklmnopqrstuvwxyz0123456789")
gc = gspread.service_account("../keys.json").open("Price Comparison Form (Responses)").sheet1
wks = gc.get_all_values()
for r in range(len(wks)):
    if wks[r][5] == "":
        gc.update_acell("F" + str(r+1), "".join([arr[random.randint(0, 35)] for c in range(16)]))
