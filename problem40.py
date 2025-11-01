# Take a number from the user and print countdown to 1 (like 5 → 5,4,3,2,1).
n=int(input("Enter the number: "))
i=n
print("Countdown=")
while i>=1:
    print(i)
    i-=1
