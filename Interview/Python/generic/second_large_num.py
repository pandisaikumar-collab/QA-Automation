# Create a list of numbers
numbers = [10, 25, 5, 40, 30]

# Assume the first element is the largest number initially
largest = numbers[0]

# Also assume the first element is the second largest initially
second = numbers[0]

# Loop through each number in the list
for num in numbers:

    # If current number is greater than largest
    if num > largest:
        # Current largest becomes second largest
        second = largest

        # Update largest with current number
        largest = num

    # If current number is not the largest
    # but greater than second largest
    elif num > second and num != largest:
        # Update second largest
        second = num

# Print the second largest number
print("Second largest:", second)

# first i assume the first element of the list is both the largest and second largest
# this is just initial setup

# then i am iterating the each number in the list
# > if the current number is grated than the largest
# > then the current largest becomes the second largest

# if the number is not grater than the largest,
# but it is grated than the second largest
# > then i update only the second largest