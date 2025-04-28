# This excercise is to modify values in dictionaries:

def update_warehouse_product_database():
    warehouse_product_database = {
        "Xbox": 77,
        "PS5": 912,
        "Switch": 311,
        "Steam Deck": 51,
        "Valve Index": 102
    }
    todays_orders = {
        "Xbox": 12,
        "PS5": 112,
        "Switch": 310,
        "Steam Deck": 51,
        "Valve Index": 62
    }

   
    # Using todays orders update the warehouse product database.
    warehouse_product_database = warehouse_product_database["Xbox"] - todays_orders["Xbox"]
    print(warehouse_product_database)
    
    warehouse_product_database = warehouse_product_database["PS5"] - todays_orders["PS5"]
    print(warehouse_product_database)

    warehouse_product_database = warehouse_product_database["Switch"] - todays_orders["Switch"]
    print(warehouse_product_database)
    
    warehouse_product_database = warehouse_product_database["Steam Deck"] - todays_orders["Steam Deck"]
    print(warehouse_product_database)

    warehouse_product_database = warehouse_product_database["Valve Index"] - todays_orders["Valve Index"]
    print(warehouse_product_database)

update_warehouse_product_database()