# Print the reverse multiplication table of any number (like 5 → 5×10 down to 5×1).
n=int(input("Enter the number for multiplication="))
i=10
while i>=1:
    print(f"{n} x {i} = {i*n}")
    i-=1