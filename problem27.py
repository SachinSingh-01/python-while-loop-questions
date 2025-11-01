# Take a number and print all its divisors (factors).
n=int(input("Enter the number to check: "))
i=1
while i<=n:
    if(n%i==0):
        print(f"Divisors={i}")
    i+=1