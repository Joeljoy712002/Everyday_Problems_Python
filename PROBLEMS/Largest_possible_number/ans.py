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