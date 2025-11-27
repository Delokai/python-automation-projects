import csv

# Read the CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    # Convert reader to a list so we can process it
    rows = list(reader)

# Remove duplicate rows
unique_rows = []
for row in rows:
    if row not in unique_rows:
        unique_rows.append(row)

# Print the unique rows
for row in unique_rows:
    print(row)
