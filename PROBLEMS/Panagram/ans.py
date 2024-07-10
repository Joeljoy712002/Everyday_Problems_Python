# panagram

def find_missing_characters(sentence):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    present_chars = set(sentence.lower())
    missing_chars = [char for char in alphabet if char not in present_chars]
    return missing_chars

if __name__ == "__main__":
    input_string = input("Enter a sentence: ")
    missing = find_missing_characters(input_string)
    
    if missing:
        print(f"Missing characters to make it a pangram: {''.join(missing)}")
    else:
        print("The sentence is already a pangram.")