first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name + " " + last_name
total_letters = len(first_name) + len(last_name)

print(f"Full Identity: {full_name}")
print(f"Total letters (excluding spaces): {total_letters}")
