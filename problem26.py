# Find the sum of odd numbers from 1 to 10.
i=1
total=0
while i<=10:
    if(i%2!=0):
        print(i)
        total=total+i
    i=i+1
print(f"The sum of odd number from 1 to 10: {total}")