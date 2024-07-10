def sortString(s):
    # Sort the characters of the string and join them into a new string
    sorted_str = ''.join(sorted(s))
    print(sorted_str)

if __name__ == '__main__':
    s = "prepbytes"
    sortString(s)



def sortStringDescending(s):
    # Sort the characters of the string in descending order and join them into a new string
    sorted_str = ''.join(sorted(s, reverse=True))
    print(sorted_str)

if __name__ == '__main__':
    s = "prepbytes"
    sortStringDescending(s)