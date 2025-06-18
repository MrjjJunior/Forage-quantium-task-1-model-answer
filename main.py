#!/bin/python3
import csv

# retrieve the data from data/daily_sales_data_0.csv
# retrieve the data from data/daily_sales_data_1.csv
# retrieve the data from data/daily_sales_data_2.csv

# filter by product name pink morsel.

# location of the data files
data1 = "data/daily_sales_data_0.csv" 
data2 = "data/daily_sales_data_1.csv"  
data3 = "data/daily_sales_data_2.csv"  

pink_morsel_data = []
'''
def filter_pink_morsel(data_file):
    
    with open(data_file, mode='r') as csv_file:
        for row in csv_file:
            if "pink morsel" in row:
                pink_morsel_data.append(row.strip().split(','))


filter_pink_morsel(data1)
filter_pink_morsel(data2)
'''

'''
pink = []

def pink_morsel_filter(data):
    with open(data, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        for line in csv_reader:
            if "pink morsel" in line:
                pink.append(line)

def make_history_file(list):
    ''' '''
    with open('pink_morsel_history.csv', mode="r") as history_file:
        csv_writer = csv.writer(history_file)
        for row in list:
            csv_writer.writerow(row)



pink_morsel_filter(data1)
pink_morsel_filter(data2)
pink_morsel_filter(data3)
make_history_file(pink)

#for row in pink:
#    print(row)
'''

def filter(data):
    with open(data, mode="r") as csv_file:

        csv_reader = csv.reader(csv_file)

        with open('history_pink_morsel.csv', mode="w") as history_file:
            csv_writer = csv.writer(history_file)
        
            for line in csv_reader:
                if "pink morsel" in line:
                    if "$" in line[1]:
                        line[1] = line[1].replace("$", "")
                        sale = f"${float(line[1]) * float(line[2]):.2f}"
                        output = sale, line[3], line[4]
                        csv_writer.writerow(output)

def open_history():
    with open('history_pink_morsel.csv', mode="r") as file:
        csv_reader = csv.reader(file)
        for line in csv_reader:
            print(line)


filter(data1)
filter(data2)
filter(data3)
open_history()
