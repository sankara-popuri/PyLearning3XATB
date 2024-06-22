# Given number
num = int(input("Enter the number:"))

# Calculate square and cube
square = num * num
cube = num * num * num

# Print the results
print(f"The square of {num} is: {square}")
print(f"The cube of {num} is: {cube}")



# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Compare the numbers
if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num1} is less than {num2}")
else:
    print(f"{num1} is equal to {num2}")
