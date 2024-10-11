lifeExpectancy = 90
daysInYear = 365
weeksInYear = 52
monthsInYear = 12

age = input("How old are you? ")
age_in_months = int(age) * monthsInYear
age_in_weeks = int(age) * weeksInYear
age_in_days = int(age) * daysInYear

print(f"You are {age_in_months} months old")

yearsRemaining = lifeExpectancy - int(age)
monthsRemaining = yearsRemaining * monthsInYear
weeksRemaining = yearsRemaining * weeksInYear
daysRemaining = yearsRemaining * daysInYear

print(f"You have {monthsRemaining} months left")
print(f"You have {weeksRemaining} weeks left")
print(f"You have {daysRemaining} days left")