# Write a program to reverse a number, e.g., if input is 1234, output should be 4321.
n=int(input("Enter the number: "))
remainder=0
rev=0
while n!=0:
    remainder =n % 10
    rev=(rev*10)+remainder
    n//=10
print(f"The reverse no. is {rev}")    