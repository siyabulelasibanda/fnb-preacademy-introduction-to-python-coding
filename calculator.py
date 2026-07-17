# Ask the user for two numbers.
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Display the operations that always work.
print("\nOperation        | Result")
print("-----------------|--------")
print(f"Addition         | {round(number1 + number2, 2)}")
print(f"Subtraction      | {round(number1 - number2, 2)}")
print(f"Multiplication   | {round(number1 * number2, 2)}")

# Division operations cannot use zero as the second number.
if number2 == 0:
    print("Division         | Cannot divide by zero")
    print("Floor division   | Cannot divide by zero")
    print("Modulus          | Cannot divide by zero")
else:
    print(f"Division         | {round(number1 / number2, 2)}")
    print(f"Floor division   | {round(number1 // number2, 2)}")
    print(f"Modulus          | {round(number1 % number2, 2)}")
