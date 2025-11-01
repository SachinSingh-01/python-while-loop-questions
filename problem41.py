# Find the product of digits in a number (example: 123 → 1×2×3=6).
n=int(input("Enter the digits to find its product: "))
mul=1
while n>0:
    digit=n%10
    mul=mul*digit
    n=n//10
print("Multiplication",mul)