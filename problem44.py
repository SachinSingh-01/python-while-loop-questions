# Take a number and print all numbers from 1 to that number which are divisible by both 2 and 3.
n=int(input("Enter the number to check: "))
i=1
print("Number divisible by 2 and 3")
while i<=n:
    if(i%2==0 and i%3==0):
        print(i)
    i+=1