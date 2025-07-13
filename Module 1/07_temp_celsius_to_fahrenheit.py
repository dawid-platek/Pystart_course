# Prepare a program that will convert temperature from Celsius to Fahrenheit.
# Tf = (Tc * 9/5) + 32  # Convert Celsius to Fahrenheit
temperature_celsius = float(input("Enter the temperature in degrees Celsius: "))
temperature_fahrenheit = (temperature_celsius * 9/5) + 32  # Convert Celsius to Fahrenheit
print(f"The temperature in Fahrenheit is: {temperature_fahrenheit:.2f}")  # Print temperature rounded to two decimal places