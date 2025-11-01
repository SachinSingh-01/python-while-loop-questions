# Write a program to print the multiplication table of any number entered by the user using a while loop.
n=int(input("Enter the number for multiplication: "))
i=1
while i<=10:
    print(f"{n} x {i}={i*n}")
    i +=1