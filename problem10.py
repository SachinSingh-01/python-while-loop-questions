<<<<<<< HEAD
# Write a program to check if a number is a palindrome (same forward and backward).
n = int(input("Enter a number: "))
original = n
rev = 0
while n > 0:
    digit = n % 10          
    rev = (rev * 10) + digit  
    n = n // 10             
if original == rev:
    print(original, "is a Palindrome number.")
else:
    print(original, "is NOT a Palindrome number.")
=======
# Write a program to check if a number is a palindrome (same forward and backward).
n = int(input("Enter a number: "))
original = n
rev = 0
while n > 0:
    digit = n % 10          
    rev = (rev * 10) + digit  
    n = n // 10             
if original == rev:
    print(original, "is a Palindrome number.")
else:
    print(original, "is NOT a Palindrome number.")
>>>>>>> 5c11fc3551f96dd9932449ddffeb3363024b7332
