



#------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------

# largest number from array 

def largestNumber(array):
    if len(array) == 1:
        return str(array[0])
    
    # Convert all elements to strings
    for i in range(len(array)):
        array[i] = str(array[i])
    
    # Sort array based on the custom comparator
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[j] + array[i] > array[i] + array[j]:
                array[i], array[j] = array[j], array[i]
    
    # Join the array to form the largest number
    result = ''.join(array)
    # Handle the case where the result is a sequence of zeros
    if result == '0' * len(result):
        return '0'
    else:
        return result

def main():
    n = int(input("Enter the number of elements in the array: "))
    array = []

    print("Enter the elements of the array:")

    for _ in range(n):
        user_input = input()
        num = int(user_input)
        array.append(num)
                
    
    result = largestNumber(array)
    print("The largest number that can be formed is:", result)

if __name__ == "__main__":
    main()

   
#------------------------------------------------------------------------------------------------------------------------------------

"""Given an array form a triangle such that the last row of the triangle contains 
all the elements of the array and the row above it will contain the sum of two elements below it."""

def form_triangle(array):
    # List to hold the rows of the triangle
    triangle = [array]
    
    # Build the triangle from the bottom to the top
    while len(triangle[0]) > 1:
        current_row = triangle[0]
        new_row = [current_row[i] + current_row[i + 1] for i in range(len(current_row) - 1)]
        triangle.insert(0, new_row)  # This line will remain the same since we need to insert at the beginning
    
    return triangle

def print_triangle(triangle):
    for row in triangle:
        print(row)

def main():
    # Input the array from the user
    array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
    
    # Form the triangle
    triangle = form_triangle(array)
    
    # Print the triangle
    print_triangle(triangle)

if __name__ == "__main__":
    main()

#------------------------------------------------------------------------------------------------------------------------------------

# max profit


def maxProfit(price):
    n = len(price)
    if n <= 1:
        return 0
    
    max_profit = 0
    min_price = price[0]

    for i in range(1, n):
        if price[i] > min_price:
            max_profit += price[i] - min_price
        min_price = price[i]

    return max_profit

if __name__ == '__main__':
     array = list(map(int, input("Enter the elements of the array separated by spaces: ").split()))
     print(maxProfit(array))


#------------------------------------------------------------------------------------------------------------------------------------

# Find the smallest and largest number in an Array

arr = [3, 1, 56, 34, 12, 9, 98, 23, 4]
minVal = min(arr)
maxVal = max(arr)

print(f"Smallest Number: {minVal}")
print(f"Largest Number: {maxVal}")

#------------------------------------------------------------------------------------------------------------------------------------

# decimal to binary 

def decimal_to_binary(decimal_num):
    # Handle special case for 0
    if decimal_num == 0:
        return '0'
    
    binary_str = ''
    while decimal_num > 0:
        binary_str = str(decimal_num % 2) + binary_str
        decimal_num //= 2
    
    return binary_str

#------------------------------------------------------------------------------------------------------------------------------------

# sub of two metrices

def subtract_matrices(mat1, mat2):
    # Check if matrices have the same dimensions
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        raise ValueError("Matrices must have the same dimensions for subtraction.")

    # Initialize a result matrix with zeros
    result = [[0 for _ in range(len(mat1[0]))] for _ in range(len(mat1))]               #rslt = [[0] * C2 for _ in range(R1)]

    # Subtract corresponding elements
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            result[i][j] = mat1[i][j] - mat2[i][j]

    return result

def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_matrix_from_user():
    matrix = []
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    print(f"Enter the {rows}x{cols} matrix:")

    for i in range(rows):
        row = []
        for j in range(cols):
            element = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(element)
        matrix.append(row)

    return matrix

if __name__ == "__main__":
    try:
        print("Enter Matrix 1:")
        mat1 = get_matrix_from_user()

        print("\nEnter Matrix 2:")
        mat2 = get_matrix_from_user()

        # Subtract matrices
        result = subtract_matrices(mat1, mat2)

        # Print matrices and result
        print("\nMatrix 1:")
        print_matrix(mat1)
        print("\nMatrix 2:")
        print_matrix(mat2)
        print("\nSubtraction Result:")
        print_matrix(result)

    except ValueError as e:
        print(e)

#------------------------------------------------------------------------------------------------------------------------------------

# check rectangles overlap 

def do_rectangles_overlap(rect1, rect2):
    # Rectangles are given as tuples (x1, y1, x2, y2)
    x1_r1, y1_r1, x2_r1, y2_r1 = rect1
    x1_r2, y1_r2, x2_r2, y2_r2 = rect2
    
    # Check for no overlap conditions
    if x1_r1 >= x2_r2 or x1_r2 >= x2_r1:
        # Check if rectangles are not horizontally overlapped
        return False
    if y1_r1 >= y2_r2 or y1_r2 >= y2_r1:
        # Check if rectangles are not vertically overlapped
        return False

    
    # If above conditions are false, then rectangles overlap
    return True

if __name__ == "__main__":
    # Example rectangles given as (x1, y1, x2, y2)
    rect1 = (0, 0, 2, 2)
    rect2 = (1, 1, 3, 3)
    
    if do_rectangles_overlap(rect1, rect2):
        print("Rectangles overlap.")
    else:
        print("Rectangles do not overlap.")


#------------------------------------------------------------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------------------------------------------------------------

""" Given that there are N books and M students. Also given are the number of pages in each book in ascending order. The task is to
assign books in such a way that the maximum number of pages assigned to a student is minimum, with the condition that every student 
is assigned to read some consecutive books. Print that minimum number of pages. """


def is_possible(books, n, m, curr_min):
    students_required = 1
    current_sum = 0

    for i in range(n):
        # If a single book has more pages than curr_min, it's not possible
        if books[i] > curr_min:
            return False
        
        # Check if adding this book to current student's allocation exceeds curr_min
        if current_sum + books[i] > curr_min:
            # Allocate books to next student
            students_required += 1
            current_sum = books[i]
            
            # If more students are required than available, return False
            if students_required > m:
                return False
        else:
            current_sum += books[i]

    return True

def find_min_pages(books, n, m):
    if n < m:
        return -1  # Not enough books to allocate one to each student

    total_pages = sum(books)
    start = max(books)
    end = total_pages
    result = float('inf')

    while start <= end:
        mid = (start + end) // 2
        
        if is_possible(books, n, m, mid):
            result = min(result, mid)
            end = mid - 1
        else:
            start = mid + 1

    return result

# Example usage:
books = [12, 34, 67, 90]  # Number of pages in each book
n = len(books)            # Number of books
m = 2                     # Number of students

print("Minimum number of pages:", find_min_pages(books, n, m))



