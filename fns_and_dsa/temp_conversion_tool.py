# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius.
    :param fahrenheit: Temperature in Fahrenheit
    :return: Temperature in Celsius
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit.
    :param celsius: Temperature in Celsius
    :return: Temperature in Fahrenheit
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        # Prompt user for input
        temp_input = input("Enter the temperature to convert: ").strip()
        if not temp_input.replace('.', '', 1).isdigit() and not temp_input.lstrip('-').replace('.', '', 1).isdigit():
            raise ValueError("Invalid temperature. Please enter a numeric value.")
        
        temperature = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temp:.2f}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temp:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

