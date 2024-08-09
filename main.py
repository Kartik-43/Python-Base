# with open('weather_data.csv') as data_file:
#    data = data_file.read()
#    print(data)

# import csv

# with open('weather_data.csv') as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        print(row)
#        if row[1] != 'Temperature':
#            temperatures.append(int(row[1]))
#    print(temperatures)

import pandas

data = pandas.read_csv('weather_data.csv')

print(data['Temperature'])
