#next permutation 

def next_permutation(s):
    # Step 1: Find the largest index i such that s[i] < s[i + 1]
    i = len(s) - 2
    while i >= 0 and s[i] >= s[i + 1]:
        i -= 1
    
    if i < 0:
        return False  # No next permutation
    
    # Step 2: Find the largest index j greater than i such that s[i] < s[j]
    j = len(s) - 1
    while s[j] <= s[i]:
        j -= 1
    
    # Step 3: Swap s[i] and s[j]
    s[i], s[j] = s[j], s[i]
    
    # Step 4: Reverse the sequence from i + 1 to the end of the string
    s[i + 1:] = reversed(s[i + 1:])
    
    return True

if __name__ == "__main__":
    s = list("prepbytes")
    if not next_permutation(s):
        print("No Word Possible")
    else:
        print("".join(s))