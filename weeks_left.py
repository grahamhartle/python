life_expectancy = 90
days_in_year = 365
weeks_in_year = 52
months_in_year = 12

age = input("How old are you? ")

age_in_months = int(age) * months_in_year
age_in_weeks = int(age) * weeks_in_year
age_in_days = int(age) * days_in_year

print(f"You are {age_in_months} months old")

years_remaining = life_expectancy - int(age)
months_remaining = years_remaining * months_in_year
weeks_remaining = years_remaining * weeks_in_year
days_remaining = years_remaining * days_in_year

print(f"You have {months_remaining} months left, {weeks_remaining} weeks left, and {days_remaining} days left.")
