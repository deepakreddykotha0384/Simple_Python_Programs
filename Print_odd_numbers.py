#   Print Odd Numbers from 1 to N

n = int(input("Enter a number: "))

print("Odd numbers from 1 to", n, "are:")
for i in range(1, n+1, 2):
    print(i)
