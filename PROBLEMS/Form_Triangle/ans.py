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