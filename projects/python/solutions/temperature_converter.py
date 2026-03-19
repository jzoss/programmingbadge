"""
⚜️ A SCOUT IS TRUSTWORTHY ⚜️
==============================
This is the COMPLETED SOLUTION for the Temperature Converter.
A Scout is trustworthy — don't peek at this until you've tried
solving the challenges on your own first!

The first point of the Scout Law reminds us to be honest and
do our best work. Give it a real try before looking here!
==============================

🌡️ Temperature Converter — SOLUTION
====================================
Programming Merit Badge — Requirement 5a (Python)

This version includes all challenges completed:
  ✅ Challenge #1: Kelvin conversion added
  ✅ Bug Fix: Error handling for non-numeric input
  ✅ Challenge #3: Loop to convert multiple temperatures
"""


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the formula: C = (F - 32) * 5/9"""
    celsius = (fahrenheit - 32) * 5 / 9
    return round(celsius, 1)


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the formula: F = C * 9/5 + 32"""
    fahrenheit = celsius * 9 / 5 + 32
    return round(fahrenheit, 1)


# ✅ Challenge #1: Celsius to Kelvin conversion
def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin using the formula: K = C + 273.15"""
    kelvin = celsius + 273.15
    return round(kelvin, 2)


def kelvin_to_celsius(kelvin):
    """Convert Kelvin to Celsius using the formula: C = K - 273.15"""
    celsius = kelvin - 273.15
    return round(celsius, 1)


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

    # ✅ Bug Fix: Error handling for non-numeric input
    while True:
        temp_str = input("  Enter the temperature (a number): ")
        try:
            temperature = float(temp_str)
            break
        except ValueError:
            print(f"  ❌ '{temp_str}' is not a valid number. Please try again!")

    # Get the unit — now includes Kelvin!
    print()
    print("  What unit is that in?")
    print("    F = Fahrenheit")
    print("    C = Celsius")
    print("    K = Kelvin")  # ✅ Challenge #1: Kelvin option
    unit = input("  Enter F, C, or K: ").strip().upper()

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
        celsius_value = result
        message = get_temperature_message(result)

    elif unit == "C":
        # Convert Celsius to Fahrenheit
        result = celsius_to_fahrenheit(temperature)
        print(f"  🌡️  {temperature}°C  =  {result}°F")
        # Use the original Celsius value for our message decisions
        celsius_value = temperature
        message = get_temperature_message(temperature)

    # ✅ Challenge #1: Kelvin conversion
    elif unit == "K":
        # Convert Kelvin to Celsius first, then show both
        celsius_result = kelvin_to_celsius(temperature)
        fahrenheit_result = celsius_to_fahrenheit(celsius_result)
        print(f"  🌡️  {temperature}K  =  {celsius_result}°C  =  {fahrenheit_result}°F")
        celsius_value = celsius_result
        message = get_temperature_message(celsius_result)

    else:
        print(f"  ❌ Sorry, I don't recognize the unit '{unit}'.")
        print("  Please enter F for Fahrenheit, C for Celsius, or K for Kelvin.")
        return

    print()
    print(f"  {message}")
    print()

    # Show some extra fun facts based on DECISIONS
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

    # ✅ Challenge #3: Loop to convert multiple temperatures
    keep_going = True

    while keep_going:
        # Step 2: Get INPUT from the user
        temperature, unit = get_user_input()

        # Step 3: Do COMPUTATIONS and DECISIONS, then show OUTPUT
        convert_and_display(temperature, unit)

        # Ask if they want to convert another temperature
        print()
        again = input("Do you want to convert another temperature? (y/n): ").strip().lower()
        if again != "y" and again != "yes":
            keep_going = False
        print()

    # Goodbye message
    print("Thanks for using the Temperature Converter! 🌡️")
    print()


# This special line means "run main() when this file is executed directly"
if __name__ == "__main__":
    main()
