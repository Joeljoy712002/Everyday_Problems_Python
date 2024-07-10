# area of incircle

import math

def area_incircle_right_triangle(a, b):
    # Step 1: Calculate hypotenuse
    c = math.sqrt(a**2 + b**2)
    
    # Step 3: Calculate radius of incircle
    r = (a + b - c) / 2
    
    # Step 4: Calculate area of incircle
    A = math.pi * r**2
    
    return A

if __name__ == "__main__":
    # Example usage:
    a = 3
    b = 4
    area = area_incircle_right_triangle(a, b)
    print(f"Area of the incircle of the right-angled triangle with legs {a} and {b} is: {area:.2f}")