num1 = float(input("Enter the first number: "))

num2 = float(input("Enter the second number: "))

# Perform arithmetic operations

addition = num1 + num2

difference = num1 - num2

product = num1 * num2

quotient = num1 / num2  # Fixed typo: 'numl' → 'num1'

remainder = num1 % num2  # Fixed spacing

exponentiation = num1 ** num2

floor_division = num1 // num2

# Display the results

print(f"\nArithmetic Operations between {num1} and {num2}:")

print(f"Sum: {num1} + {num2} = {addition}")  # Fixed: Moved to new line
print(f"Difference: {num1} - {num2} = {difference}")

print(f"Product: {num1} * {num2} = {product}")

print(f"Quotient: {num1}/{num2} = {quotient}")

print(f"Remainder: {num1}% {num2} = {remainder}")

print(f"Exponentiation: {num1} ** {num2} = {exponentiation}")

print(f"Floor Division: {num1} // {num2} = {floor_division}")

num_str = input("Enter a number: ")

print("\nData Type Conversion:")

# Convert string to integer
num_int = int(num_str)
print(f"String to Integer: {num_str} → {num_int}")

# Convert string to float
num_float = float(num_str)
print(f"String to Float: {num_str} → {num_float}")

# Convert integer to float
int_to_float = float(num_int)
print(f"Integer to Float: {num_int} → {int_to_float}")

# Convert float to integer
float_to_int = int(num_float)
print(f"Float to Integer: {num_float} → {float_to_int}")

# Convert integer to string
int_to_str = str(num_int)
print(f"Integer to String: {num_int} → {int_to_str}")

# Convert float to string
float_to_str = str(num_float)
print(f"Float to String: {num_float} → {float_to_str}")

# Convert integer to boolean (0 is False, any other number is True)
int_to_bool = bool(num_int)
print(f"Integer to Boolean: {num_int} → {int_to_bool}")

# Convert string to boolean (empty string is False, any other string is True)
str_to_bool = bool(num_str)
print(f"String to Boolean: '{num_str}' → {str_to_bool}")
