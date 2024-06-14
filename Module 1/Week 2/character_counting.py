def count_chars(string):
    """
    Count the occurrences of each character in the given string.

    Args:
    string (str): The input string to count characters from.

    Returns:
    dict: A dictionary with characters as keys and their counts as values, sorted by character.
    """
    # Initialize an empty dictionary to store character counts
    counting_dict = dict()

    # Iterate over each character in the string
    for character in string:
        # If the character is already in the dictionary, increment its count
        if character in counting_dict.keys():
            counting_dict[character] += 1
        # If the character is not in the dictionary, add it with a count of 1
        else:
            counting_dict[character] = 1

    # Create a new dictionary sorted by character keys
    sorted_counting_dict = {key: counting_dict[key]
                            for key in sorted(counting_dict.keys())}

    # Return the sorted dictionary
    return sorted_counting_dict


# Test Cases
string = "Happiness"
# Output: {'H': 1, 'a': 1, 'e': 1, 'i': 1, 'n': 1, 'p': 2, 's': 1}
print(count_chars(string))
string = "smiles"
print(count_chars(string))  # Output: {'e': 1, 'i': 1, 'l': 1, 'm': 1, 's': 2}
