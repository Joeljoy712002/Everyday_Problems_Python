# swap arrays 

def main():
    a = [11, 12, 13, 14]
    b = [15, 16, 17, 18]

    # Swapping the arrays
    a, b = b, a

    print("a[] =", end=" ")
    for elem in a:
        print(elem, end=", ")

    print("\nb[] =", end=" ")
    for elem in b:
        print(elem, end=", ")

if __name__ == "__main__":
    main()