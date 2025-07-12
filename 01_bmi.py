height = int(input("Enter your height in centimeters: "))
weight = int(input("Enter your weight in kilograms: "))

height_meters = height / 100  # Convert # height to meters
bmi = weight / (height_meters ** 2)  # Calculate BMI

print(f"Your BMI is: {bmi:.2f}")  # Print BMI rounded to two decimal places

# This code calculates the Body Mass Index (BMI) based on the user's height and weight.