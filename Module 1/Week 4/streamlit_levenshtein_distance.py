import streamlit as st
import numpy as np

def load_vocab(file_path):
    """
    Load vocabulary from a file and return a sorted list of unique words.

    Args:
        file_path (str): Path to the vocabulary file.

    Returns:
        list: A sorted list of unique words.
    """
    with open(file_path, 'r') as file:
        words = {line.strip() for line in file}
    return sorted(words)

def levenshtein_distance(source, target):
    """
    Calculates the Levenshtein distance between two strings.

    Args:
        source (str): The source string.
        target (str): The target string.

    Returns:
        int: The Levenshtein distance between the two strings.
    """
    delete_len, insert_len = len(source) + 1, len(target) + 1
    distance_matrix = np.zeros((delete_len, insert_len), dtype=np.uint8)

    distance_matrix[:, 0] = np.arange(delete_len, dtype=np.uint8)
    distance_matrix[0, :] = np.arange(insert_len, dtype=np.uint8)

    for delete_axis in range(1, delete_len):
        for insert_axis in range(1, insert_len):
            candidate_1 = distance_matrix[delete_axis - 1, insert_axis] + 1
            candidate_2 = distance_matrix[delete_axis, insert_axis - 1] + 1
            sub_cost = 0 if target[insert_axis - 1] == source[delete_axis - 1] else 1
            candidate_3 = distance_matrix[delete_axis - 1, insert_axis - 1] + sub_cost
            distance_matrix[delete_axis, insert_axis] = min(candidate_1, candidate_2, candidate_3)

    return distance_matrix[delete_len - 1, insert_len - 1]

def main():
    """
    Main function to run the Streamlit application for word correction using Levenshtein distance.
    """
    vocabs = load_vocab(file_path='./Module 1/Week 4/materials/vocab.txt')

    st.title("Word Correction using Levenshtein Distance")
    word = st.text_input("Word: ")

    if st.button("Compute"):
        levenshtein_distances = {vocab: levenshtein_distance(word, vocab) for vocab in vocabs}
        sorted_distances = dict(sorted(levenshtein_distances.items(), key=lambda item: item[1]))
        correct_word = next(iter(sorted_distances))

        st.markdown(f"### Correct Word: {correct_word}")
        
        col1, col2 = st.columns(2)
        col1.write('Vocabulary:')
        col1.write(vocabs)
        col2.write('Distances:')
        col2.write(sorted_distances)

if __name__ == "__main__":
    main()