# Find the sum of all digits until a single digit remains (Example: 987 → 9+8+7=24 → 2+4=6)
n=int(input("Enter the digit: "))
while n>=10:
    total=0
    while n>0:
        digit=n%10
        total+=digit
        n=n//10
    n=total
    print("Sum", n)