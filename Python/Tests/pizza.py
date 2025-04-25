# This is an excercise in copying and changing a copied list:

pizzas = ["Pepperoni Pizza", "Hawaiian Pizza", "Cheeseburger Pizza"]
print(pizzas)



for pizza in pizzas:
    print(f"I like {pizza}")
print("I really love pizza!")
    

friends_pizza = pizzas[:]

pizzas.append("Godfather Pizza")
friends_pizza.append("Capricosa Pizza")

print(pizzas)
print(friends_pizza)

print(f"My favourite pizzas are: {pizzas}")
print(f"My friend's favourite pizzas are: {friends_pizza}")
