import csv
import pandas as pd


drivers = 'C:\\Users\\grayson\\Documents\\project-folder\\python\\playground\\nascar.csv'
output = 'C:\\Users\\grayson\\Documents\\project-folder\\python\\playground\\nascarTrans.csv'


# data = [line.strip() for line in open(drivers, 'r')]

# print(data)
df = pd.read_csv(drivers, sep=',', names= ['currentPosition','carNumber', 'driver', 'startPosition', 'laps not-mobile', 'laps-led not-mobile', 'final-status', 'points not-mobile'])
print(df)




# f = open(drivers, 'r')
# with f:
#     reader = csv.reader(f)
#     for row in reader:
#         for e in row:
#             print(e)