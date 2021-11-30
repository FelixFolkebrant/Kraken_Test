import pandas as pd
from datetime import datetime
import csv
  
  
# field names 

filename = "./ETHUSDC_1.csv"

df = pd.read_csv(filename)
df = df.values.tolist()

for x in range(len(df)):
    df[x][0] = datetime.fromtimestamp(df[x][0])
    print(df[x][0])


headers = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume', 'Trades'] 
  
# with open('updated.csv', 'w') as f:
      
#     # using csv.writer method from CSV package
#     write = csv.writer(f)
      
#     write.writerow(headers)
#     write.writerows(df)

with open('updated.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(df)