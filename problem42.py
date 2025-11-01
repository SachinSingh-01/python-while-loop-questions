# Count how many even digits are in a given number.
n=int(input("Enter the digits: "))
count=0
even_digits=[]
while n>0:
    digit=n%10
    if  digit%2==0:
        count+=1
        even_digits.append(digit)

    n=n//10
print("Number of even digit=", count)
print("Even number=",even_digits[::-1])