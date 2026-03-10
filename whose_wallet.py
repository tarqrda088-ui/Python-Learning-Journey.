import random

names_string = input("Give me everybody's names, separated by a comma: ")
names = names_string.split(", ")

# Professional way to pick a random element
person_who_will_pay = random.choice(names)

print(f"{person_who_will_pay} is going to buy the meal today!")
