import csv


def open_file(file):

    with open(file, mode="r") as csv_file:
        csv_reader = csv.reader(csv_file)

        with open("combined.csv", mode="a") as combined_files:

            csv_writer = csv.writer(combined_files)
            
            for line in csv_reader:
                if line[0] == "pink morsel":
                    csv_writer.writerow(line)
    
             

#open_file("data/daily_sales_data_0.csv")

def combine_files(*args):

    for file in args:
        open_file(file)


#combine_files("data/daily_sales_data_0.csv","data/daily_sales_data_0.csv","data/daily_sales_data_0.csv")

def data_processing(*args):    
    for file in args:
        with open(file, mode="r") as csv_file:

            csv_reader = csv.reader(csv_file)

            with open("combined.csv", mode="a") as combined_files:

                csv_writer = csv.writer(combined_files)
                
                for line in csv_reader:
                    if line[0] == "pink morsel":
                        if "$" in line[1]:
                            line[1] = line[1].replace("$", "")
                            sales = f"${float(line[1]) * int(line[2]):.2f}"
                            row = sales, line[3], line[4]
                            csv_writer.writerow(row)

                 

data_processing("data/daily_sales_data_0.csv","data/daily_sales_data_1.csv","data/daily_sales_data_2.csv")