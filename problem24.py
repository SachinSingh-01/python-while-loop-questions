'''Print this pattern using while loop:
*
**
***
****
*****'''
n=int(input("Enter number of rows:"))
i=1
while i<=n:
    print("*" * i)
    i+=1