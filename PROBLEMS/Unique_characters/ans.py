# number of unique characters 

def countUniqueCharacters(s):
    # Create a set to store unique characters
    unique_chars = set(s)
    
    # Return the number of unique characters
    return len(unique_chars)

if __name__ == '__main__':
    s = "prepbytes"
    num_unique = countUniqueCharacters(s)
    print(f"The number of unique characters in '{s}' is {num_unique}.")