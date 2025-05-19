from datetime import datetime

#today = datetime.today().date()

today = datetime.strptime("2025-05-19", "%Y-%m-%d").date()

birth_date = input("Enter your date of birth (yyyy-mm-dd): ")

birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()

days_lived = (today - birth_date).days

print(f"Today's date is {today}")
print(f"Parsed birth date is: {birth_date}")
print(f"You have been alive for {days_lived} days!")

diff = today - birth_date
print(f"Difference: {diff}")
print(f"Days lived: {diff.days}")