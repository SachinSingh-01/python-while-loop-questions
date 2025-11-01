# Count how many digits are in a number (e.g., 345 → 3 digits).
n=int(input("Enter the number: "))
count=0
while n>0:
    count+=1
    n=n//10
print("No. of digit=", count)