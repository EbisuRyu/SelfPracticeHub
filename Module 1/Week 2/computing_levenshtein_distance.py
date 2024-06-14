import numpy as np


def levenshtein_distance(source: str, target: str):
    """
    Calculates the Levenshtein distance between two strings.

    The Levenshtein distance is a metric for measuring the difference between
    two sequences. It is the minimum number of single-character edits
    (insertions, deletions, or substitutions) required to change one word into the other.

    Args:
        source (str): The source string.
        target (str): The target string.

    Returns:
        np.ndarray: The distance matrix representing the Levenshtein distance between the two strings.
    """

    # Length of the source and target strings + 1 for the matrix dimensions
    delete_len = len(source) + 1
    insert_len = len(target) + 1

    # Initialize the distance matrix with the appropriate shape
    distance_matrix = np.ndarray(
        shape=(delete_len, insert_len), dtype=np.uint8)

    # Initialize the first column and first row of the matrix
    distance_matrix[:, 0] = np.arange(delete_len, dtype=np.uint8)
    distance_matrix[0, :] = np.arange(insert_len, dtype=np.uint8)

    def distance_matrix_element_computing(delete_axis, insert_axis):
        """
        Computes the value for a given cell in the distance matrix.

        Args:
            delete_axis (int): The current row index in the distance matrix.
            insert_axis (int): The current column index in the distance matrix.

        Returns:
            int: The computed value for the cell.
        """
        # Compute the possible values from neighboring cells
        candidate_1 = distance_matrix[delete_axis -
                                      1][insert_axis] + 1  # Deletion
        # Insertion
        candidate_2 = distance_matrix[delete_axis][insert_axis - 1] + 1
        sub_cost = 0 if target[insert_axis -
                               1] == source[delete_axis - 1] else 1  # Substitution
        # Substitution or match
        candidate_3 = distance_matrix[delete_axis -
                                      1][insert_axis - 1] + sub_cost

        # Return the minimum of the three candidates
        return min(candidate_1, candidate_2, candidate_3)

    # Fill in the rest of the distance matrix
    for delete_axis in range(1, delete_len):
        for insert_axis in range(1, insert_len):
            distance_matrix[delete_axis][insert_axis] = distance_matrix_element_computing(
                delete_axis, insert_axis)

    return distance_matrix[delete_len - 1][insert_len - 1]


# Example usage
print(levenshtein_distance('yu', 'you'))
