class Solution(object):
    def romanToInt(self, s):
        # Dictionary to store the mapping of Roman numerals to integers
        roman_to_int = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        
        # Initialize the total value
        total = 0
        
        # Iterate through the string
        for i in range(len(s)):
            # If current value is less than the next value, subtract it
            if i < len(s) - 1 and roman_to_int[s[i]] < roman_to_int[s[i + 1]]:
                total -= roman_to_int[s[i]]
            else:
                total += roman_to_int[s[i]]
        
        return total