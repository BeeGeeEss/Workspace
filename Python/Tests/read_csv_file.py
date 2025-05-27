import csv

"""Importing a CSV file to read it"""

with open('order.csv', mode='r', encoding='utf-8') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            pass
            line_count += 1
        print(f'\t{row["item"].title()}  {row["unit_price"].title()}  {row["qty"].title()}.')
        line_count += 1
    print(f'Processed {line_count} lines.')