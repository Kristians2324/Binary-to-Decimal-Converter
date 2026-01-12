# Function to convert binary to decimal for Max
def binary_to_decimal(binary_string):
    decimal_value = 0
    power = 0
    # We reverse the string to process from right to left (2^0, 2^1, etc.)
    for digit in reversed(binary_string):
        if digit == '1':
            decimal_value += 2 ** power
        power += 1
    return decimal_value
# Get user input
user_input = input("Enter a binary number: ")
result = binary_to_decimal(user_input)
print("The decimal result is:", result)