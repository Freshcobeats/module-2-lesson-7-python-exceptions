def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def temp():
    try:
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
    except ValueError:
        print("Please enter a valid number.")
    else:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    finally:
        print("Thank you for using the weather forecast application.")
