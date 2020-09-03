# read the csv file and extract important data like dates and assignments

import pandas as pd

dates = ["Jan", "January", "Feb", "February", "Mar", "March", "Apr", "April", "May", "Jun", "June", "Jul", "July", "Aug", "August", "Sep", "Sept", "September", "Oct", "October", "Nov", "November", "Dec", "December"]

df = pd.read_csv('output.csv')
#print(df)

event_array = []

for index, row in df.iterrows():
    if row.equals(dates):
        event_array.append(row)

print(str(event_array))

