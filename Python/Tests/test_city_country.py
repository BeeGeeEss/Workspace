#Pytest to check that the function get_city_country in the file city_country works

from city_country import get_city_country

def test_city_country():
    "Does this generate a string containing a city and country?"
    formatted_location = get_city_country('Santiago', 'Chile')
    assert formatted_location == 'Santiago, Chile'