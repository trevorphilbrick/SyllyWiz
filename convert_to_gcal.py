# read the csv file and extract important data like dates and assignments

import pandas as pd

dates = ["Jan", "January", "Feb", "February", "Mar", "March", "Apr", "April", "May", "Jun", "June", "Jul", "July", "Aug", "August", "Sep", "Sept", "September", "Oct", "October", "Nov", "November", "Dec", "December"]

df = pd.read_csv('output.csv') # set a conditional to determine of this is a docx(future update)
#print(df)

event_array = []

for index, row in df.iterrows():
    print(row)
    if row.index == 2:
        event_array.append(row)

print(str(event_array))