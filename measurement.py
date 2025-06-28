def length_converter():
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} kilometers is equal to {miles:.2f} miles.\n")

def weight_converter():
    kg = float(input("Enter weight in kilograms: "))
    pounds = kg * 2.20462
    print(f"{kg} kilograms is equal to {pounds:.2f} pounds.\n")

def temperature_converter():
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.\n")

def main():
    while True:
        print("🔁 Unit Converter")
        print("1. Length (Kilometers ↔ Miles)")
        print("2. Weight (Kilograms ↔ Pounds)")
        print("3. Temperature (Celsius ↔ Fahrenheit)")
        print("4. Exit")

        choice = input("Choose an option (1–4): ")
        print()

        if choice == '1':
            length_converter()
        elif choice == '2':
            weight_converter()
        elif choice == '3':
            temperature_converter()
        elif choice == '4':
            print("👋 Exiting Unit Converter. Goodbye!")
            break
        else:
            print("❌ Invalid input. Please choose from 1 to 4.\n")

if __name__ == "__main__":
    main()
