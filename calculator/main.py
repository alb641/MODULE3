from calculator.operations import add, subtract, multiply, divide


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid number. Please enter a number.")


def get_operation():
    while True:
        operation = input(
            "\nChoose an operation (+, -, *, /) or type 'q' to quit: "
        ).strip().lower()

        if operation in ("q", "quit"):
            return None

        if operation in ("+", "add"):
            return "add"

        if operation in ("-", "subtract"):
            return "subtract"

        if operation in ("*", "multiply"):
            return "multiply"

        if operation in ("/", "divide"):
            return "divide"

        print("Invalid operation. Please choose +, -, *, or /.")


def calculate(a, b, operation):
    if operation == "add":
        return add(a, b)

    if operation == "subtract":
        return subtract(a, b)

    if operation == "multiply":
        return multiply(a, b)

    if operation == "divide":
        return divide(a, b)

    raise ValueError("Invalid operation.")


def run_calculator():
    print("Welcome to the Python Calculator!")

    while True:
        operation = get_operation()

        if operation is None:
            print("Goodbye!")
            break

        first_number = get_number("Enter the first number: ")
        second_number = get_number("Enter the second number: ")

        try:
            result = calculate(first_number, second_number, operation)
            print(f"Result: {result}")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    run_calculator()