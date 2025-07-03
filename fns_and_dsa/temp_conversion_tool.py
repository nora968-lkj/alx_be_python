CELSIUS_TO_FAHRENHEIT_FACTOR=9/5
FAHRENHEIT_TO_CELSIUS_FACTOR=5/9

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

try:
    temp=float(input("Enter the temperature to convert: "))
    unit=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
    if unit=="C":
        result=convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")
    elif unit=="F":
        result=convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")
    else:
        raise ValueError("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")
