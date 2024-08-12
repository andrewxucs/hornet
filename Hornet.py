import itertools
import string

def load_dictionary(file_path):
    """Load dictionary words from a file."""
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def generate_variations(base_password, max_length=2):
    """Generate variations of the base password by appending digits and special characters."""
    variations = set()
    characters = string.ascii_letters + string.digits + string.punctuation
    for length in range(1, max_length + 1):
        for combination in itertools.product(characters, repeat=length):
            variations.add(base_password + ''.join(combination))
    return variations

def hybrid_attack(dictionary_file, target_password):
    """Perform a hybrid attack to guess the target password."""
    dictionary = load_dictionary(dictionary_file)
    
    # Check if the target password is in the dictionary
    if target_password in dictionary:
        return f"Password found in dictionary: {target_password}"
    
    # Check for variations of each dictionary password
    for password in dictionary:
        variations = generate_variations(password)
        if target_password in variations:
            return f"Password found in variations: {target_password}"
    
    return "Password not found"

def main():
    dictionary_file = 'dictionary.txt'  # Path to your dictionary file
    target_password = input("Enter the password to guess: ")  # User inputs the password
    
    result = hybrid_attack(dictionary_file, target_password)
    print(result)

if __name__ == "__main__":
    main()