num = int(input("Input a number to check prime or not: "))

if num <= 1:
    prime = False
else:
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
            break

if prime:
    print("The entered number is a prime number.")
else:
    print("The entered number is not a prime number.")
