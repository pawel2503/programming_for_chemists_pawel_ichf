from operations import *

result = 0

while True:
    print("\n--- Calculator ---")
    print("Choose operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Square (^2)")
    print("6. Square root (√)")
    print("7. Pi (π)")
    print("8. Clear (C)")
    print("A. surface_circle")
    print("9. Exit")
    print("______________")

    choice = input("Enter your choice (1-9): ")

    if choice == "9":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers.")
            continue

    elif choice in ["5", "6", "A"]:
        try:
            a = float(input("Enter number: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

    match choice:
        case "1": result = add(a, b)
        case "2": result = subtract(a, b)
        case "3": result = multiply(a, b)
        case "4": result = divide(a, b)
        case "5": result = square(a)
        case "6": result = root(a)
        case "7": result = pi()
        case "8": result = clear()
        case "A": result = surface_circle(a)
        case _:
            print("Invalid choice!")
            continue

    if result is not None:
        display(result)