# Thevnin's Theorem Code

import sys

# Constants
DEFAULT_VALUE = 0

def main():
    try:
        # Get input values
        voltage = float(input("Enter the voltage (V): "))
        resistance_r1 = float(input("Enter the resistance R1 (Ohms): "))
        resistance_r2 = float(input("Enter the resistance R2 (Ohms): "))

        # Input validation
        if resistance_r1 < 0 or resistance_r2 < 0:
            raise ValueError("Resistance values cannot be negative.")
        if resistance_r1 == 0 or resistance_r2 == 0:
            raise ZeroDivisionError("Resistance values cannot be zero.")

        # Calculate Thevnin equivalent voltage and resistance
        v_thevnin = voltage * (resistance_r2 / (resistance_r1 + resistance_r2))
        r_thevnin = (resistance_r1 * resistance_r2) / (resistance_r1 + resistance_r2)

        # Display results
        print(f"Thevnin Equivalent Voltage: {v_thevnin:.2f} V")
        print(f"Thevnin Equivalent Resistance: {r_thevnin:.2f} Ohms")

    except ValueError as e:
        print(f"Input Error: {str(e)}")
    except ZeroDivisionError as e:
        print(f"Calculation Error: {str(e)}")
    except Exception as e:
        print(f"Unexpected Error: {str(e)}")

# Execute the main function if this script is run directly
if __name__ == '__main__':
    main()