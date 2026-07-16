print("=== Exception Handling Demo ===")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2

    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Please enter valid integers.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Program finished.")