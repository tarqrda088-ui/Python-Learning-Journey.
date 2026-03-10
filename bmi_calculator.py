# A program to calculate Body Mass Index (BMI)
height = float(input("Enter your height in meters (e.g., 1.75): "))
weight = float(input("Enter your weight in kg: "))

# Calculation with correct math priority
bmi = weight / (height * height)

print(f"Your BMI is: {round(bmi, 2)}")
