import datetime
import calendar 

# Prompt a user to enter the month and day of their birthday, 
# print what day of the week their birthday falls on this year.
month_of_birth = int(input("Enter your birth month (1-12): "))

day_of_birth = int(input("Enter your birth day (1-31): "))

#Current year
this_year = datetime.datetime.now().year

#Birthday this year
birthday = datetime.date(this_year, month_of_birth, day_of_birth)

#index for the day of birthday this year (0 = Monday etc)
day_of_the_week = birthday.weekday()

#The day of the person's birthday this year!
day_this_year = calendar.day_name[day_of_the_week]


print("Your birthday falls on a", day_this_year, "in", this_year)




#Could be done like this:
#day_of_week = calendar.day_name[datetime.date(2023, (int(user_month)), (int(user_day))).weekday()]
#print(f"Your birthday falls on a {day_of_week} in 2023!")








