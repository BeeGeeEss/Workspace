import sys
import random
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

VALID_CITIES = ['sydney', 'melbourne', 'brisbane', 'perth']

class WeatherAPI:
    """Simulates fetching weather from an API."""
    def __init__(self, city):
        self.city = city.lower()

    def get_weather(self):
        if self.city not in VALID_CITIES:
            raise ValueError("City not supported.")
        weather = random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])
        return f"The weather in {self.city.title()} is {weather}."

def get_user_city():
    city = input(Fore.YELLOW + "Enter a city (Sydney, Melbourne, Brisbane, Perth): ")
    return city.strip()

def main():
    print(Fore.CYAN + Style.BRIGHT + "=== Welcome to the Weather CLI App ===")

    while True:
        try:
            city = get_user_city()
            if city.lower() == "quit":
                print(Fore.GREEN + "Goodbye!")
                break

            api = WeatherAPI(city)
            forecast = api.get_weather()
            print(Fore.MAGENTA + forecast)

        except ValueError as ve:
            print(Fore.RED + f"[Error] {ve}")
        except KeyboardInterrupt:
            print(Fore.RED + "\nApp interrupted. Exiting.")
            sys.exit()
        except Exception as e:
            print(Fore.RED + f"[Unexpected Error] {e}")

        print()  # blank line between interactions

if __name__ == "__main__":
    main()
