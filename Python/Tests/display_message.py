#This excercise is to call a function:
def display_message():
    """Display message about learning materials"""
    print("I'm learning about functions in Python")


display_message()


#This excercise is to call a function with a value:
def favourite_book(title):
    """Print favourite book title"""
    print(f"My favourite book is {title}")


favourite_book('Dicey\'s Song')


#This excercise is to call a function with positional arguments:
def make_shirt(shirt_size, shirt_message):
    """Display shirt size and shirt message so that we can make the shirt"""
    print(f"\nI am making your shirt!")
    print(f"\tYour shirt will be - size {shirt_size} with {shirt_message} on it")

make_shirt('medium', 'I love NY')



#This excercise is to call a function with keyword arguments:
def make_shirt(shirt_size, shirt_message):
    """Display shirt size and shirt message so that we can make the shirt"""
    print(f"\nI am making your shirt!")
    print(f"\tYour shirt will be - size {shirt_size} with {shirt_message} on it")

make_shirt(shirt_size='medium', shirt_message='I love NY')


#This excercise is to call a function with default arguments:
def make_shirt(shirt_size='large', shirt_message='I love Python'):
    """Display shirt size and shirt message so that we can make the shirt"""
    print(f"\nI am making your shirt!")
    print(f"\tYour shirt will be - size {shirt_size} with {shirt_message} on it")

make_shirt()
make_shirt(shirt_size='medium', shirt_message='I love NY')




#This excercise is to call cities within and out of the default country:
def describe_city(city, country="Iceland"):
    print(f"{city} is in {country}")


describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('Paris', 'France')



#This excercise is to return a dictionary in a fucntion:
def city_country(city_name, country_name):
    destination = {'City': city_name, 'Country': country_name}
    return destination

holiday_vibes = city_country('Barcelona', 'Spain')
holiday_vibes = city_country('Venice', 'Italy')
holiday_vibes = city_country('England', 'London')
print(holiday_vibes)



#This excercise is to add an optional argument:
def locations(city_name, country_name, town_name=None):
 
    holiday_location = {'City': city_name, 'Country': country_name}
    if town_name:
        holiday_location['Town'] = town_name
    return holiday_location


holiday_fun = locations('Paris', 'France', town_name='Chitto')
print(holiday_fun)



#This excercise is creating a function in a while loop:
def city_country(city_name, country_name):
    """Return city and country, neatly formatted"""
    destination = f"{city_name}, {country_name}"
    return destination.title()

while True:
    print(f"\nPlease tell me the city name: ")
    print("(enter q at any time to quit)")

    city = input("City: ")
    if city == 'q':
        break
    
    country = input("Country: ")
    if country == 'q':
        break


formatted_country_city = city_country(city, country)
print(f"{city}, {country}")


