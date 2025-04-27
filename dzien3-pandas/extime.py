import pandas as pd

date_sale = pd.read_csv("../data-sets/date_sale.csv", parse_dates=["Sale_Date"], date_format="%d-%m-%Y")

print(date_sale)
date_sale.info()

date_temp = pd.read_csv("../data-sets/date_temp.csv", parse_dates=["Reading_Date"], date_format="%Y/%m/%d")

print(date_temp)
date_temp.info()