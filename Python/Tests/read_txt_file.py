def show_shopping_list(filename='shopping_list.txt'):
    """Defining a function for calling a shopping list"""

    with open(filename, 'r', encoding='utf-8') as f:
        for item in f:
            print(f"* {item.strip()}")

show_shopping_list(filename='shopping_list.txt')