import re

HISTORY_FILE = "history.txt"

def show_history():
    try:
        with open(HISTORY_FILE, 'r') as file:
            lines = file.readlines()
            if not lines:
                print("No history found")
            else:
                for line in reversed(lines):
                    print(line.strip())
    except FileNotFoundError:
        print("No history found")

def clear_history():
    with open(HISTORY_FILE, 'w') as file:
        pass
    print("History cleared.")

def save_to_history(equation, result):
    with open(HISTORY_FILE, 'a') as file:
        file.write(f"{equation} = {result}\n")

def calculate(user_input):
    # Remove spaces to handle inputs like 8+8
    user_input = user_input.replace(" ", "")
    match = re.match(r"(-?\d+(\.\d+)?)([+\-*/])(-?\d+(\.\d+)?)", user_input)
    if not match:
        print("Invalid input. Use format: number operator number (e.g 8+8)")
        return

    num1 = float(match.group(1))
    op = match.group(3)
    num2 = float(match.group(4))

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        result = num1 / num2
    else:
        print("Invalid operator. USE ONLY + - * /")
        return

    if result.is_integer():
        result = int(result)
    print("Result:", result)
    save_to_history(f"{num1} {op} {num2}", result)

def main():
    print("SIMPLE CALCULATOR (Type history, clear, or exit)")
    while True:
        user_input = input("Enter calculation (+ - * /) or command (history, clear, exit): ").lower()
        if user_input == 'exit':
            print("GOOD BYE")
            break
        elif user_input == 'history':
            show_history()
        elif user_input == 'clear':
            clear_history()
        else:
            calculate(user_input)

main()
