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