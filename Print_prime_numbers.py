
# Input the upper limit N
N = int(input("Enter a number: "))

# Loop through numbers from 2 to N
for num in range(2, N + 1):
    # Check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:  # If num is divisible by i, it's not prime
            break
    else:
        # If the loop completes without finding a divisor, it's prime
        print(num)
