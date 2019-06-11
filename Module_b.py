for a in ("Apples", "Cookies", "Ice Cream", "Steak"):
    print(a)

for b in ("---"):
    print(b)

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
print("Hello, %s %s." %(first_name, last_name))

age_in_years = float(input("How old are you? "))
age_in_days = age_in_years * 365
age_in_weeks = age_in_years * 52
age_in_months = age_in_years * 12
print("You're at least %s days old." %(age_in_days))
print("You're at least %s weeks old" %(age_in_weeks))
print("You're at least %s months old" %(age_in_months))

print(b)
print(b)
print(b)

pillow = input("Enter a noun:")
whirl = input ("Enter a verb:")
fancy = input("Enter an adjective:")
stadium = input("Enter a place:")
print("Take your %s %s and %s it at a %s!" %(fancy, pillow, whirl, stadium))