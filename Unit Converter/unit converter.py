# ----------------------------------------------
# 📌 Python Unit Converter App (Static, No DB)
# Categories: Length, Weight, Temperature, Time
# ----------------------------------------------

# Conversion factors stored in dictionaries
length_units = {
    "km": 1000,     # 1 km = 1000 m
    "m": 1,         # Base unit = meter
    "cm": 0.01,
    "mm": 0.001,
    "mile": 1609.34,
    "ft": 0.3048,
    "inch": 0.0254
}

weight_units = {
    "kg": 1000,     # 1 kg = 1000 g
    "g": 1,         # Base unit = gram
    "mg": 0.001,
    "lb": 453.592,
    "ounce": 28.3495
}

time_units = {
    "day": 86400,   # 1 day = 86400 seconds
    "hour": 3600,
    "min": 60,
    "sec": 1        # Base unit = second
}

# ----------------------------------------------
# 🔹 Temperature conversion needs formulas
# ----------------------------------------------
def convert_temperature(value, from_unit, to_unit):
    # Normalize input unit to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5/9
    elif from_unit == "K":
        celsius = value - 273.15
    else:
        return "Invalid temperature unit!"

    # Convert Celsius to target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return (celsius * 9/5) + 32
    elif to_unit == "K":
        return celsius + 273.15
    else:
        return "Invalid temperature unit!"


# ----------------------------------------------
# 🔹 General conversion function (Length, Weight, Time)
# ----------------------------------------------
def convert_units(value, from_unit, to_unit, unit_dict):
    try:
        # Convert input to base unit
        base_value = value * unit_dict[from_unit]
        # Convert base unit to target unit
        return base_value / unit_dict[to_unit]
    except KeyError:
        return "Invalid unit entered!"


# ----------------------------------------------
# 🔹 Main Menu System
# ----------------------------------------------
def main():
    while True:
        print("\n===== UNIT CONVERTER APP =====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Time")

        
        choice = input("Choose a category (1-4): ")
        
        if choice == "1":
            print("\nLength Units: km, m, cm, mm, mile, ft, inch")
            val = float(input("Enter value: "))
            f = input("From unit: ")
            t = input("To unit: ")
            result = convert_units(val, f, t, length_units)
            print(f"{val} {f} = {result} {t}")
        
        elif choice == "2":
            print("\nWeight Units: kg, g, mg, lb, ounce")
            val = float(input("Enter value: "))
            f = input("From unit: ")
            t = input("To unit: ")
            result = convert_units(val, f, t, weight_units)
            print(f"{val} {f} = {result} {t}")
        
        elif choice == "3":
            print("\nTemperature Units: C, F, K")
            val = float(input("Enter value: "))
            f = input("From unit: ")
            t = input("To unit: ")
            result = convert_temperature(val, f, t)
            print(f"{val} {f} = {result} {t}")
        
        elif choice == "4":
            print("\nTime Units: day, hour, min, sec")
            val = float(input("Enter value: "))
            f = input("From unit: ")
            t = input("To unit: ")
            result = convert_units(val, f, t, time_units)
            print(f"{val} {f} = {result} {t}")
        
        else:
            print("Invalid choice! Please select from 1-4.")


# ----------------------------------------------
# 🔹 Run the App
# ----------------------------------------------
if __name__ == "__main__":
    main()
