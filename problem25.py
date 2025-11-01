# Find the sum of even numbers from 1 to 10.
i=2
total=0
while i<=10:
    if(i%2==0):
        print(i)
        total+=i
    i+=1
print(f"The sum of even number from 1 to 10:{total}")