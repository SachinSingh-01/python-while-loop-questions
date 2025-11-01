# Take a number and check if it is a Strong number.(Example: 145 → 1!+4!+5!=145)
n=int(input("Enter the number: "))
original=n
total=0
while n>0:
    digit=n%10
    fact=1
    i=1
    while i<=digit:
        fact=fact*i
        i+=1
    total=total+fact
    n=n//10
if total==original:
    print("It is a Strong number")
else:
    print("It is not Strong number")