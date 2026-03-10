# Converting minutes to hours and remaining minutes
total_minutes = int(input("Enter total minutes to convert: "))

hours = total_minutes // 60
minutes = total_minutes % 60

print(f"{total_minutes} minutes equals {hours} hours and {minutes} minutes.")

