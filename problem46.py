# Keep asking user for numbers and find their total sum, stop when user types 0.
total = 0
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    total += n
print("Sum =", total)
print("Loop ended because you entered 0")
