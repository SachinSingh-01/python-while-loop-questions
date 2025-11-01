# Take a number and check if it is an Armstrong number.(Example: 153 → 1³+5³+3³=153 → Yes)
n=int(input("Enter the number: "))
original=n
i=1
total=0
while n>0:
    digit=n%10
    total=total+(digit**3)
    n=n//10
    i+=1
print(total)
if total==original:
    print("Its is a armstrong number")
else:
    print("Not a armstrong number")