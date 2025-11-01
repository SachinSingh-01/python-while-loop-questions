# Keep taking input from the user until they enter 0.
# Start the loop
num = int(input("Enter a number (0 to stop): "))
while num != 0:        
    print("You entered:", num)
    num = int(input("Enter a number (0 to stop): ")) 
print("Loop ended because you entered 0.")
