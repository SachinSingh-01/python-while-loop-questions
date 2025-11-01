# Take a number and find its square sum (example: 3 → 1²+2²+3² = 14).
n=int(input("Enter the number to find its square: "))
i=1
total=0
while i<=n:
    total=total+(i*i)
    i+=1
print(total)
