# addind number from 1 to 100

sum = 0
for number in range(1, 101):
    sum += number
print(f"Sum of all number from 1 to 100 is: {sum}")

# range(a, b, c) -> a is the starting point, b is the ending point (exclusive), c is the step (optional, default is 1)
# range(1, 101) -> it will generate a sequence of numbers from 1 to 100 (inclusive) with a step of 1.
# range(1, 101, 2) -> it will generate a sequence of numbers from 1 to 100 (inclusive) with a step of 2 (1, 3, 5, 7, ...)

