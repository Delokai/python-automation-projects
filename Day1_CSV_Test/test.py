import csv

# Open the CSV file in "read" mode
with open("data.csv", "r") as file:
    reader = csv.reader(file)

    # Loop through each row in the CSV
    for row in reader:
        print(row)