"""
🌡️ Temperature Converter
========================
Programming Merit Badge — Requirement 5a (Python)

This program converts temperatures between Fahrenheit and Celsius.
It takes user input, performs calculations, makes decisions, and
produces output — all the things a good program should do!

Run this program:
    python3 temperature_converter.py
"""


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9"""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the formula: F = C * 9/5 + 32"""
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)


# TODO Challenge #1: Add a function to convert Celsius to Kelvin!
# Formula: K = C + 273.15
# def celsius_to_kelvin(celsius):
#     ...


def get_temperature_message(celsius):
    """
    Make DECISIONS based on the temperature!
    Returns a fun message depending on how hot or cold it is.
    """
    if celsius <= 0:
        return "🥶 Brrrr! That's FREEZING! Water turns to ice at this temperature!"
    elif celsius <= 10:
        return "🧥 That's cold! Better wear a warm jacket!"
    elif celsius <= 20:
        return "😊 Nice and cool — perfect for a hike!"
    elif celsius <= 30:
        return "☀️ Warm and pleasant — great day to be outside!"
    elif celsius <= 40:
        return "🥵 That's HOT! Stay hydrated and find some shade!"
    else:
        return "🔥 EXTREME HEAT! That's dangerously hot — stay inside!"


def display_welcome():
    """Show the welcome banner."""
    print("=" * 50)
    print("   🌡️  TEMPERATURE CONVERTER  🌡️")
    print("   Programming Merit Badge — Req 5a")
    print("=" * 50)
    print()


def get_user_input():
    """
    Get temperature and unit from the user.
    This is the INPUT part of our program.
    """
    print("What temperature do you want to convert?")
    print()

    # Get the temperature value
    # 🐛 INTENTIONAL BUG: What happens if the user types "abc" instead of a number?
    # Can you add error handling to fix this?
    temp_str = input("  Enter the temperature (a number): ")
    temperature = float(temp_str)

    # Get the unit
    print()
    print("  What unit is that in?")
    print("    F = Fahrenheit")
    print("    C = Celsius")
    # TODO Challenge #1: Add Kelvin as an option here!
    unit = input("  Enter F or C: ").strip().upper()

    return temperature, unit


def convert_and_display(temperature, unit):
    """
    Perform the COMPUTATION and make DECISIONS.
    Then display the OUTPUT.
    """
    print()
    print("-" * 50)

    if unit == "F":
        # Convert Fahrenheit to Celsius
        result = fahrenheit_to_celsius(temperature)
        print(f"  🌡️  {temperature}°F  =  {result}°C")
        # Use Celsius value for our message decisions
        message = get_temperature_message(result)

    elif unit == "C":
        # Convert Celsius to Fahrenheit
        result = celsius_to_fahrenheit(temperature)
        print(f"  🌡️  {temperature}°C  =  {result}°F")
        # Use the original Celsius value for our message decisions
        message = get_temperature_message(temperature)

    # TODO Challenge #1: Add an elif for Kelvin here!

    else:
        print(f"  ❌ Sorry, I don't recognize the unit '{unit}'.")
        print("  Please enter F for Fahrenheit or C for Celsius.")
        return

    print()
    print(f"  {message}")
    print()

    # Show some extra fun facts based on DECISIONS
    if unit == "F":
        celsius_value = result
    else:
        celsius_value = temperature

    print("  📊 Fun Facts:")
    if celsius_value == 0:
        print("     ❄️ That's exactly the freezing point of water!")
    elif celsius_value == 100:
        print("     💨 That's exactly the boiling point of water!")
    elif celsius_value == 37:
        print("     🤒 That's normal human body temperature!")
    elif celsius_value < 0:
        print(f"     🧊 That's {abs(celsius_value)}° below freezing!")
    elif celsius_value > 100:
        print(f"     ♨️ That's {celsius_value - 100}° above boiling!")

    print("-" * 50)


# ============================================================
# MAIN PROGRAM
# This is where the program starts running!
# ============================================================

def main():
    """Main function — runs the temperature converter."""

    # Step 1: Show the welcome screen
    display_welcome()

    # Step 2: Get INPUT from the user
    temperature, unit = get_user_input()

    # Step 3: Do COMPUTATIONS and DECISIONS, then show OUTPUT
    convert_and_display(temperature, unit)

    # Goodbye message
    print()
    print("Thanks for using the Temperature Converter! 🌡️")
    print()

    # TODO Challenge #3: Add a loop here so the user can convert
    # multiple temperatures without restarting the program!
    # Hint: Use a while loop and ask "Do you want to convert another? (y/n)"


# This special line means "run main() when this file is executed directly"
if __name__ == "__main__":
    main()
