import csv

"""Importing a CSV file to read it, and append another order"""

def display_order():
    """Defining a function that reads the order, subtotals to 2 decimal points"""
    with open('order.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        total = 0
        for row in csv_reader:
            unit_price = float(row['unit_price'])
            qty = int(row['qty'])
            subtotal = unit_price * qty
            total += subtotal
            print(f"{row["qty"].title()} x {row["item"].title()} @ ${unit_price:.2f} = {subtotal:.2f}.")
            


def add_item(item, unit_price, qty):
    """Defining a function to append a new order to the existing order"""
    with open('order.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Chips', 6.5, 1])


"""Ensures that code only runs when executed directly, not on import"""
if __name__ == '__main__':
    add_item('Chips', 6.5, 1)
    display_order()
