# Find the sum of digits of a number (e.g., 123 → 6).
n=int(input("Enter the number to find sum: "))
total=0
while n>0:
    digit=n%10
    total+=digit
    n=n//10
print("Sum", total)
