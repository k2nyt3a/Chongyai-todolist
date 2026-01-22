def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculate_velocity(distance: float, time: float) -> float:
    if time <= 0:
        raise ValueError("Time must be greater than zero")
    return distance / time

if __name__ == "__main__":
    while True:
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Velocity")
        print("6. Exit")
        choice = input("Enter choice (1/2/3/4/5/6): ")
        if choice == '6':
            break
        if choice in ['1','2','3','4','5']:
            try:
                if choice == '5':
                    num1 = float(input("Enter distance: "))
                    num2 = float(input("Enter time: "))
                else:
                    num1 = float(input("Enter first number: "))
                    num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"{num1} / {num2} = {result}")
        elif choice == '5':
            try:
                result = calculate_velocity(num1, num2)
                print(f"Velocity = {result}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Invalid choice. Please select 1-6.")