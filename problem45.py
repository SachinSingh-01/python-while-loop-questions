# Print the Fibonacci series up to n terms.
n = int(input("Number of terms= "))
a = 0
b = 1
count = 0

print("Fibonacci Series:")

while count < n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1