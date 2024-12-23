

def length_conversion():
    print("Select operation:")
    print("    1.Meter() ↔ Centimeter()")
    print("    2.Meter() ↔ Feet()")
    print("    3.Kilometer() ↔ Miles()")
    try:
        choice = int(input("Enter 1 or 2 or 3: "))
        match choice:
            case 1:
                print("From:\n   1.Meter TO Centimeter.\n    2.Centimeter TO Meter.")
                try:
                    unit = int(input("Enter op: "))
                    match unit:
                        case 1:
                            meter = float(input("Enter the value in Meters: "))
                            centimeter = meter * 100
                            print(f"\n{meter:.2f} meters is equal to {centimeter:.2f} centimeters.")
                        case 2:
                            centimeter = float(input("Enter the value in Centimeter: "))
                            meter= centimeter / 100
                            print(f"\n{centimeter:.2f} centimeter is equal to {meter:.2f} Meter.")
                        case _:
                            print("Enter: 1 or 2")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            case 2:
                print("From:\n   1.Meter TO Feet.\n    2.Feet TO Meter.")
                try:
                    unit = int(input("Enter op: "))
                    match unit:
                        case 1:
                            meter = float(input("Enter the value in Meters: "))
                            Feet = meter * 3.28084
                            print(f"\n{meter:.2f} meters is equal to {Feet:.2f} Feet.")
                        case 2:
                            Feet = float(input("Enter the value in Feet: "))
                            meter = Feet * 0.3048
                            print(f"\n{Feet:.2f} Feet is equal to {meter:.2f} Meter.")
                        case _:
                            print("Enter: 1 or 2")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            case 3:
                print("From:\n   1.Kilometer TO Miles.\n    2.Miles TO kilometer.")
                try:
                    unit = int(input("Enter op: "))
                    match unit:
                        case 1:
                            kilometer = float(input("Enter the value in kilometers: "))
                            mile = kilometer * 0.621371
                            print(f"\n{kilometer:.2f} kilometers is equal to {mile:.2f} miles.")
                        case 2:
                            mile = float(input("Enter the value in Miles: "))
                            kilometer = mile * 1.60934
                            print(f"\n{mile:.2f} miles is equal to {kilometer:.2f} kilometer.")
                        case _:
                            print("Enter: 1 or 2")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            case _:
                print("Invalid choice, Range(1,2,3)")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
def Mass_conversion():
    print("Select operation:")
    print("    1.Gram(g) ↔ Kilogram(Kg)")
    print("    2.Kilogram(Kg) ↔ Pounds")
    try:
        choice = int(input("Enter 1 or 2: "))
        match choice:
            case 1:
                print("From:\n   1.Gram TO Kilogram.\n    2.Kilogram TO Gram.")
                try:
                    unit = int(input("Enter op: "))
                    match unit:
                        case 1:
                            grams = float(input("Enter the value of grams."))
                            kilogram = grams / 1000
                            print(f"\n{grams:.2f} grams is equal to {kilogram:.2f} Kilogram.")
                        case 2:
                            kilogram = float(input("Enter the value of kilogram."))
                            grams = kilogram * 1000
                            print(f"\n{kilogram:.2f} Kilogram is equal to {grams:.2f} Grams.")
                        case _:
                            print("Enter: 1 or 2")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            case 2:
                print("From:\n   1.Kilogram TO Pounds.\n    2.Pounds TO Kilogram.")
                try:
                    unit = int(input("Enter op: "))
                    match unit:
                        case 1:
                            kilogram = float(input("Enter the value of Kilogram."))
                            Pounds = kilogram * 2.20462
                            print(f"\n{kilogram:.2f} Kilogram is equal to {Pounds:.2f} Pounds.")
                        case 2:
                            Pounds = float(input("Enter the value of Pounds."))
                            kilogram = Pounds / 2.20462
                            print(f"\n{Pounds:.2f} Pounds is equal to {kilogram:.2f} Kilogram.")
                        case _:
                            print("Enter: 1 or 2")
                except ValueError:
                    print("Invalid input. Please enter numeric values.")
            case _:
                print("Invalid choice, Range(1,2)")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
def time_conversion():
    print("Select operation:    [ From: .. To: .. ]")
    print("    1.Second(Sec) ↔Minute(Min) ↔Hour(H)")
    print("    2.     1      ↔     2      ↔   3   ")
    try:
        choice1, choice2 = int(input("From: ")), int(input("To: "))
        if choice1==1 and choice2==2:   #from: sec to: min
            sec = int(input("Enter the value in seconds: "))
            min = sec / 60
            print(f"\n{sec} seconds is equal to {min:.2f} minutes.")
        elif choice1==1 and choice2==3:   #from: sec to: hour
            sec = int(input("Enter the value in seconds: "))
            hour = sec / 3600
            print(f"\n{sec} seconds is equal to {hour:.2f} hours.")
        elif choice1==2 and choice2==1:   #from: min to: sec
            min = int(input("Enter the value in minutes: "))
            sec = min * 60
            print(f"\n{min} minutes is equal to {sec} seconds.")
        elif choice1==2 and choice2==3:   #from: min to: hour
            min = int(input("Enter the value in minutes: "))
            hour = min / 60
            print(f"\n{min} minutes is equal to {hour:.2f} hours.")
        elif choice1==3 and choice2==1:   #from: hour to: sec
            hour = int(input("Enter the value in hours: "))
            sec = hour * 3600
            print(f"\n{hour} hours is equal to {sec} seconds.")
        elif choice1==3 and choice2==2:   #from: hour to: min
            hour = int(input("Enter the value in hours: "))
            min = hour * 60
            print(f"\n{hour} hours is equal to {min} minutes.")
        else:
            print("Invalid choice. Please select from the options available.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
def temperature_conversion():
    print("Select operation:    [ From: .. To: .. ]")
    print("    1.Celsius(C) ↔ Fahrenheit(F) ↔ Kelvin(K) )")
    print("    2.    1   ↔     2      ↔   3   ")
    try:
        choice1, choice2 = int(input("From: ")), int(input("To: "))
        if choice1==1 and choice2==2:   #from: C to: F
            Celsius = float(input("Enter the temperature in Celsius: "))
            Fahrenheit = (Celsius * 9/5) + 32
            print(f"\n{Celsius:.2f}°C is equal to {Fahrenheit:.2f}°F.")
        elif choice1==1 and choice2==3:   #from: C to: K
            Celsius = float(input("Enter the temperature in Celsius: "))
            Kelvin = Celsius + 273.15
            print(f"\n{Celsius:.2f}°C is equal to {Kelvin:.2f}K.")
        elif choice1==2 and choice2==1:   #from: F to: C
            Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            Celsius = (Fahrenheit - 32) * 5/9
            print(f"\n{Fahrenheit:.2f}°F is equal to {Celsius:.2f}°C.")
        elif choice1==2 and choice2==3:   #from: F to: K
            Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
            Kelvin = (Fahrenheit - 32) * 5/9 + 273.15
            print(f"\n{Fahrenheit:.2f}°F is equal to {Kelvin:.2f}K.")
        elif choice1==3 and choice2==1:   #from: K to: C
            Kelvin = float(input("Enter the temperature in Kelvin: "))
            Celsius = Kelvin - 273.15
            print(f"\n{Kelvin:.2f}K is equal to {Celsius:.2f}°C.")
        elif choice1==3 and choice2==2:   #from: K to: F
            Kelvin = float(input("Enter the temperature in Kelvin: "))
            Fahrenheit = (Kelvin - 273.15) * 9/5 + 32
            print(f"\n{Kelvin:.2f}K is equal to {Fahrenheit:.2f}°F.")
        else:
            print("Invalid choice. Please enter a valid option.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

while True:
    print("Select operation:")
    print("    1.Length conversion")
    print("    2.Mass conversion")
    print("    3.Time conversion")
    print("    4.Temperature conversion")
    print("    5.Exit")
    user = input("Enter your choice: ").lower()
    if user in ["length", "1"]:
        length_conversion()
    elif user in ["mass", "2"]:
        Mass_conversion()
    elif user in ["time", "3"]:
        time_conversion()
    elif user in ["temperature", "4"]:
        temperature_conversion()
    elif user in ["exit", "5"]:
        break
    else:
        print("For select operation, Enter : 1 or 2 or 3 or 4 ")