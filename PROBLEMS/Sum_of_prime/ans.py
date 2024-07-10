# prime up to n numbers sum

def is_prime(num):
    """Function to check if a number is prime."""
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # Even numbers greater than 2 are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def sum_of_primes(N):
    """Function to find the sum of all prime numbers between 1 and N."""
    prime_sum = 0
    for number in range(2, N + 1):
        if is_prime(number):
            prime_sum += number
    return prime_sum

if __name__ == "__main__":
    N = int(input("Enter a number (N): "))
    if N < 2:
        print("N should be greater than or equal to 2")
    else:
        result = sum_of_primes(N)
        print(f"The sum of all prime numbers between 1 and {N} is: {result}")