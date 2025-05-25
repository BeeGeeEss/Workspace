class Restaurant:
    """A class for a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise attributes to describe a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Method describing the restaurant"""
        description = f"{self.restaurant_name}, {self.cuisine_type}"
        return description
    
    def open_restaurant(self):
        """Method letting people know that the restaurant is open"""
        open = f"{self.restaurant_name} is now open!"
        return open
    
    def count_customers(self):
        """Method calling the default attribute for customers served"""
        print(f"The number of guests served is {self.number_served}")
    
    def set_number_served(self, customers):
        """Method for setting number of customers served"""
        self.set_number_served = customers
    

my_restaurant = Restaurant('400Gradi', 'Italian')
your_restaurant = Restaurant('Hoo Gah', 'Cafe-Style')
our_restaurant = Restaurant('Salt', 'Gourmet')
the_restaurant = Restaurant('Clove', 'Organic')

print(my_restaurant.describe_restaurant())
print(my_restaurant.open_restaurant())

print(your_restaurant.describe_restaurant())
print(your_restaurant.open_restaurant())

print(our_restaurant.describe_restaurant())
print(our_restaurant.open_restaurant())

print(the_restaurant.describe_restaurant())
print(the_restaurant.open_restaurant())

"""Calling the default attribute for guests served"""
print(f"The number of guests served is {the_restaurant.number_served}")
"""Setting the default nummber for guests served"""
the_restaurant.number_served = 10
print(f"The number of guests served is {the_restaurant.number_served}")
"""Set the default number by calling a new method"""
the_restaurant.set_number_served(15)
print(f"The number of guests served is {the_restaurant.set_number_served}")



"""Creating a class from a class and inheriting parent attributes"""
class IceCreamStand(Restaurant):
    """Represents an ice cream stand modelled off a restaurant class"""

    def __init__(self, restaurant_name, cuisine_type, flavours):
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours
    
    def describe_flavours(self):
        flavour = f"{self.restaurant_name} provides {self.flavours} flavours!"
        return flavour


st_augustus = IceCreamStand('St. Augustus', 'Ice-creamery', 'strawberry & chocolate')
print(st_augustus.describe_restaurant())
print(st_augustus.describe_flavours())





class User:
    """Class of users in a game"""

    def __init__(self, first_name, last_name, age, level, login_attempts=0):
        """Attributes of users in a game"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.level = level
        self.login_attempts = login_attempts
    
    def describe_user(self):
        """Method for calling all user information"""
        description = f"User: {self.first_name} {self.last_name}, is {self.age}, and plays at user level: {self.level}"
        return description
    
    def greet_user(self):
        """Say hello to our users"""
        greet = f"Welcome, {self.first_name}!"
        return greet
    
    def increment_login_attempts(self):
        """Method to only allow 3 login attempts"""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Method that resets the user login"""
        self.login_attempts = 0

user1 = User("Billy", "Holden", "24", "Beginner")
user2 = User("Brianna", "Berry", "20", "Intermediate")
user3 = User("Barry", "Logan", "45", "Expert")

print(user1.describe_user())
print(user1.greet_user())
print(user2.describe_user())
print(user2.greet_user())
print(user3.describe_user())
print(user3.greet_user())

user1.increment_login_attempts()
print(f"{user1.first_name}'s login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"{user1.first_name}'s login attempts: {user1.login_attempts}")
user1.increment_login_attempts()
print(f"{user1.first_name}'s login attempts: {user1.login_attempts}")
user1.reset_login_attempts()
print(f"{user1.first_name}'s login reset: {user1.login_attempts}")



class Admin(User):

    def __init__(self, first_name, last_name, age, level, login_attempts=0, privileges=None):
        super().__init__(first_name, last_name, age, level, login_attempts)
        self.privileges = privileges

        if privileges is None:
            self.privileges = ['can add post', 'can delete post', 'can ban user']
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("Admin privileges:")
        for privilege in self.privileges:
            print({privilege})


admin1 = Admin("Alice", "Smith", 35, "Admin")
admin1.show_privileges()