# fibunocci

def fibonacci(n):
    fib_sequence = []
    
    if n >= 1:
        fib_sequence.append(0)  # The first Fibonacci number is 0
    if n >= 2:
        fib_sequence.append(1)  # The second Fibonacci number is 1
    
    for i in range(2, n):
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
    return fib_sequence

def main():
    n = int(input("Enter the number of Fibonacci numbers to generate: "))
    
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fib_sequence = fibonacci(n)
        print(f"The first {n} Fibonacci numbers are:")
        for num in fib_sequence:
            print(num, end=" ")
        print()

if __name__ == "__main__":
    main()
